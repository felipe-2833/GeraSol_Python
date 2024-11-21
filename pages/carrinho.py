import streamlit as st 
from datetime import datetime, timedelta
import time
import json
import requests
from modules.database.catalogo import visualizar_gerador
from modules.database.carrinho import visualizar_pedido, visualizar_itens, visualizar_alugueis

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
    tab1, tab2= st.tabs(["Compras", "Alugueis"])
    with tab1:
        for pedido in lista_compras:
            if pedido['idUsuario'] == st.session_state.id:
                for item in lista_itens_pedidos:
                    if item.get("idPedido") == pedido.get("idPedido"):
                        item_pedido = item
                with st.expander(f"{visualizar_gerador(item_pedido.get("idGerador")).get("modelo")}"):
                    st.write(f"Valor: {item_pedido.get("valorUnitario")}")
                    st.write(f"Quantidade: {item_pedido.get("quantidade")}")
                    st.write(f"Preço Total: {pedido.get("totalPedido")}")
                    st.write(f"Data do Pedido: {pedido.get("dataPedido")}")
    with tab2:
        for pedido in lista_aluguel:
            if pedido['idUsuario'] == st.session_state.id:
                for item in lista_itens_pedidos:
                    if item.get("idPedido") == pedido.get("idPedido"):
                        item_pedido = item
                for i in lista_trans_aluguel:
                    if i.get("idPedido") == pedido.get("idPedido"):
                        aluguel = i
                with st.expander(f"{visualizar_gerador(item_pedido.get("idGerador")).get("modelo")}"):
                    st.write(f"Valor diario: {aluguel.get("valorDiario")}")
                    st.write(f"Quantidade: {item_pedido.get("quantidade")}")
                    st.write(f"Dias Alugados: {aluguel.get("diasAluguel")}")
                    st.write(f"Preço Total: {aluguel.get("totalAluguel")}")
                    st.write(f"Data Inicio: {aluguel.get("dataInicio")}")
                    st.write(f"Data Fim: {aluguel.get("dataFim")}")
                   
   