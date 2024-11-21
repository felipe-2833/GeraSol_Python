import streamlit as st 
import time
import json
from modules.utils.utils import pula_linha, adiciona_lista_enderecos
from modules.database.usuario import visualizar, visualizar_user
from modules.database.enderecos import visualizar_enderecos, apagar_endereco
from modules.dialog.dialogs_user import infos_user, atualizar_user, apagar_user_adv
from modules.dialog.dialogs_endereco import infos_endereco, cadastrar_endereco, atualizar_endereco

lista_users = visualizar()
lista_enderecos = visualizar_enderecos()
key_counter = 0
endereco_counter = 0

st.title("login:")
with st.container(height=200):
    email = st.text_input("E-mail: ", placeholder="Digite seu e-mail")
    senha = st.text_input("Senha: ", placeholder="Crie uma senha", type="password")
    
if st.button("Login"):
    for user in lista_users:
        if user["email"] == email and user["senha"] == senha:
            st.session_state.login = True
            st.session_state.id = user["idUsuario"]
        else:
            st.session_state.login = False
            st.session_state.id = None
    if st.session_state.login:
        st.session_state.message_login = "Usuario logado!"
    else:
        st.error("Usuario não encontrado!")

if st.session_state.login:
    user = visualizar_user(st.session_state.id)
    st.success(st.session_state.message_login)
    if st.button("Info Login"):
        infos_user(st.session_state.id)
    if st.button("alterar infos"):
        atualizar_user(st.session_state.id)
    if st.button("apagar conta"):
        apagar_user_adv(st.session_state.id)
        
    json_data = json.dumps(user, indent=4)

    st.download_button(
        label="Baixar JSON",
        data=json_data,
        file_name="dados_user.json",
        mime="application/json"
    )
    st.header("Enderecos Cadastrados:")
    for endereco in lista_enderecos:
        id = endereco["idEndereco"]
        if endereco["enderecoIdUser"] == st.session_state.id:
            endereco_counter += 1
            with st.expander(f"{endereco.get("rua")}, {endereco.get("numero")}"):
                key_counter += 1
                if st.button(label="Infos",key=key_counter):
                    infos_endereco(id)
                key_counter += 1
                if st.button(label="Atualizar",key=key_counter):
                    atualizar_endereco(id)
                key_counter += 1
                if st.button(label="Deletar",key=key_counter):
                    apagar_endereco(id) 
                    st.success("Endereco deletado com sucesso.")
                    time.sleep(1)
                    st.rerun()
    if endereco_counter == 0:
        st.write("Nenhum endereço cadastrado")
    key_counter += 1
    if st.button(label="Cadastrar endereco",key=key_counter):
                    cadastrar_endereco(id)
    st.session_state.lista_enderecos = adiciona_lista_enderecos(visualizar_enderecos(), st.session_state.id, st.session_state.lista_enderecos)
    
        

