import streamlit as st 
from datetime import datetime, timedelta
import time
import json
import requests
from modules.utils.utils import adiciona_pedido_carrinho, pula_linha
from modules.database.carrinho import visualizar_pedido, visualizar_itens, visualizar_alugueis
from modules.dialog.dialogs_carrinho import comprar_gerador

lista_pedidos = visualizar_pedido()
lista_trans_aluguel = visualizar_alugueis()
lista_compras = []
for pedido in lista_pedidos:
    if pedido.get("tipoTransacao") == "Venda":
        lista_compras.append(pedido)
lista_aluguel = []
for pedido in lista_pedidos:
    if pedido.get("tipoTransacao") == "Aluguel":
        lista_aluguel.append(pedido)
lista_itens_pedidos = visualizar_itens()
item_pedido = {}
aluguel = {}
key_counter = 0



st.title("Carrinho")

if st.session_state.id == None and st.session_state.login == False:
    st.warning("Necessario fazer login para visualização dos seus pedidos")
    
else:
    tab1, tab2, tab3= st.tabs(["Pendentes", "Concluidos", "Cancelados"])
    with tab1:
        preco = adiciona_pedido_carrinho(lista_compras, lista_itens_pedidos,lista_aluguel, lista_trans_aluguel, "Pendente")
        pula_linha(3)
        if st.button("Comprar"):
            comprar_gerador(st.session_state.lista_enderecos, preco)
    with tab2:
        adiciona_pedido_carrinho(lista_compras, lista_itens_pedidos,lista_aluguel, lista_trans_aluguel, "Concluido")     
    with tab3:
        adiciona_pedido_carrinho(lista_compras, lista_itens_pedidos,lista_aluguel, lista_trans_aluguel, "Cancelado")
                    
   