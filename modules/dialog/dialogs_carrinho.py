import streamlit as st 
from datetime import datetime,timedelta
import requests
import json
import time
from modules.utils.utils import atualizar_pedido_dialog

@st.dialog("Comprar Gerador")
def comprar_gerador(lista_enderecos, preco):
    endereco = st.selectbox("Endereço", lista_enderecos, index= None, placeholder="Escolha o endereço cadastrado que será utilizado")
    cartao = st.selectbox("Cartão", ["Visa - final 4376"], index= None, placeholder="Escolha o cartão que será utilizado")
    st.write(f"Preço Total da compra: {preco}")
    if lista_enderecos == []:
        st.warning("Nenhum endereço cadastrado, cadastre enderecos na pagina de login.")
    elif preco == 0:
        st.warning("Nenhum pedido no carrinho")
    else:
        if not (endereco and cartao):
            st.warning("Preencha todos os campos.")
        else:
            if st.button("Concluir compra"):
                atualizar_pedido_dialog(st.session_state.id)
                st.success("Pedido comprado com sucesso!")
                time.sleep(2)
                st.rerun()