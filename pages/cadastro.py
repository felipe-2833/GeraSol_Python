import streamlit as st 
from datetime import datetime, timedelta
import time
import json
import requests
from modules.database.usuario import criar_cliente

st.title("Cadastro:")
with st.container(height=400):
    nome_completo = st.text_input("Nome Completo:", placeholder="Digite seu nome completo")
    email = st.text_input("E-mail:", placeholder="Digite seu e-mail")
    senha = st.text_input("Senha:", placeholder="Crie uma senha", type="password")
    telefone = st.text_input("Telefone:", placeholder="Digite seu telefone com DDD")
    
    # Campo para a data de nascimento
    max_date = datetime.today()  # Data máxima é hoje
    min_date = datetime.today() - timedelta(days=100 * 365)  # Data mínima: 100 anos atrás
    data_de_nascimento = st.date_input(
        "Data de Nascimento:", 
        value=datetime.today(), 
        min_value=min_date.date(), 
        max_value=max_date.date()
    )
   
if st.button("Cadastrar"):
    data_formatada = data_de_nascimento.strftime("%Y-%m-%d")
    cadastro ={
    "nomeCompleto": nome_completo,
    "email": email,
    "senha": senha,
    "telefone": telefone,
    "dataNascimento": data_formatada,
    }
    try:
        resposta_api = criar_cliente(cadastro)
        st.success("usuario cadastrado com sucesso")
        time.sleep(5)
        st.rerun()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 422:
            st.error("Erro de validação: os dados enviados não estão corretos.")
        else:
            st.error(f"Erro ao criar a tarefa: {err}")
        
        st.write("Resposta da API:", err.response.text)

    except json.JSONDecodeError:
        st.error("Erro ao processar a resposta da API. Resposta inválida.")

    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {e}")
    