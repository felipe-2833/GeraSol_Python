import streamlit as st 
from datetime import datetime,timedelta
import requests
import json
import time
from modules.database.usuario import visualizar_user, atualiza_user
from modules.utils.utils import apagar_user_total
            
@st.dialog("Atualizar informações do usuário:")
def atualizar_user(id: int):
    user = visualizar_user(id)
    nome_completo = st.text_input("Nome Completo:", value=user["nomeCompleto"])
    email = st.text_input("E-mail:", value=user["email"])
    senha = st.text_input("Senha:", value=user["senha"], type="password", placeholder="Crie uma nova senha")
    telefone = st.text_input("Telefone:", value=user["telefone"])
    data_nascimento_obj = datetime.strptime(user["dataNascimento"], "%Y-%m-%d")
    min_date = datetime.today() - timedelta(days=100 * 365)  # Data mínima: 100 anos atrás
    max_date = datetime.today()  # Data máxima: hoje
    data_nascimento_atualizada = st.date_input(
        "Data de Nascimento:", 
        value=data_nascimento_obj, 
        min_value=min_date.date(), 
        max_value=max_date.date()
    )
    data_nascimento_formatada = data_nascimento_atualizada.strftime("%Y-%m-%d")
    
    if st.button("Atualizar"):
        user_new = {
            "nomeCompleto": nome_completo,
            "email": email,
            "senha": senha,
            "telefone": telefone,
            "dataNascimento": data_nascimento_formatada
        }
        
        try:
            atualiza_user(id, user_new)
            st.success("Usuário atualizado com sucesso!")
            time.sleep(2)
            st.rerun()
        
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                st.error("Erro de validação: os dados enviados não estão corretos.")
            else:
                st.error(f"Erro ao atualizar o usuário: {err}")
            st.write("Resposta da API:", err.response.text)
        
        except json.JSONDecodeError:
            st.error("Erro ao processar a resposta da API. Resposta inválida.")
        
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")
    
@st.dialog("Infos User")
def infos_user(id: int):
    user = visualizar_user(id) 
    st.write(f"Nome Completo: {user['nomeCompleto']}")
    st.write(f"E-mail: {user['email']}")
    st.write(f"Telefone: {user['telefone']}")
    data_nascimento = user.get("dataNascimento")
    data_formatada = data_nascimento.replace("-", "/")
    st.write(f"Data de Nascimento: {data_formatada}")
    
@st.dialog("Deseja realmente apagar a tarefa?")
def apagar_user_adv(id):
    st.write("Caso apague este usuario, todas as informações referentes a ele serão perdidas.")
    if st.button("Apagar"):
        apagar_user_total(id) 
        st.success("User deletado com sucesso.")
        time.sleep(1)
        st.session_state.login = False
        st.session_state.id = None
        st.rerun()
    if st.button("Voltar"):
        st.rerun()

    
    
