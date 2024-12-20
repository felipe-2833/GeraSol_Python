import streamlit as st 
import time
import requests
import json
import random
from modules.database.catalogo import visualizar_gerador,visualizar_pedidos
from modules.database.carrinho import atualiza_pedido
from modules.database.usuario import apagar_user, visualizar_user
from modules.database.enderecos import apagar_endereco, visualizar_enderecos
from modules.database.carrinho import apagar_aluguel,apagar_itens_pedido,apagar_pedido, visualizar_alugueis,visualizar_itens,visualizar_pedido

lista_alugueis = visualizar_alugueis()
lista_itens = visualizar_itens()
lista_pedidos = visualizar_pedido()
lista_enderecos = visualizar_enderecos()

#Função para pular linhas dependendo do numero passado
def pula_linha(n:int):
    for i in range(0,n):
        st.write(" ")
        
def adiciona_lista_enderecos(lista:list[dict], id, lista_session) -> list:
    new_list = []
    for endereco in lista:
        if endereco["enderecoIdUser"] == id:
            new_list.append(f"{endereco.get("rua")}, {endereco.get("numero")}")
    if new_list == lista_session:
        return lista_session
    else:
        return new_list

def cancelar_pedido(id:int, pedido:dict):
    if pedido['idUsuario'] == id:
        id_pedido = pedido['idPedido']
        id_usuario = pedido["idUsuario"]
        data_pedido = pedido["dataPedido"]
        status = "Cancelado"
        total_pedido = pedido["totalPedido"]
        tipo_transacao = pedido["tipoTransacao"]
        data_entrega = pedido["dataEntrega"]
        

    
        pedido_new = {
            "idUsuario": id_usuario,
            "dataPedido": data_pedido,
            "status": status,
            "totalPedido": total_pedido,
            "tipoTransacao": tipo_transacao,
            "dataEntrega": data_entrega
        }

        try:
            atualiza_pedido(id_pedido, pedido_new)
            print("ok!")
        
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                st.error("Erro de validação: os dados enviados não estão corretos.")
            else:
                st.error(f"Erro ao atualizar o pedido: {err}")
            st.write("Resposta da API:", err.response.text)
        
        except json.JSONDecodeError:
            st.error("Erro ao processar a resposta da API. Resposta inválida.")
        
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")
        
def adiciona_pedido_carrinho(lista_compras:list[dict], lista_itens_pedidos:list[dict],lista_aluguel:list[dict], lista_trans_aluguel:list[dict], status:str) -> float:
    preco = 0
    contador = 0
    st.header("Itens Para Compra:")
    for pedido in lista_compras:
        if pedido['idUsuario'] == st.session_state.id and pedido["status"] == status:
            contador += 1
            for item in lista_itens_pedidos:
                if item.get("idPedido") == pedido.get("idPedido"):
                    item_pedido = item
            with st.expander(f"{visualizar_gerador(item_pedido.get("idGerador")).get("modelo")}"):
                st.write(f"Valor: {item_pedido.get("valorUnitario")}")
                st.write(f"Quantidade: {item_pedido.get("quantidade")}")
                st.write(f"Preço Total: {pedido.get("totalPedido")}")
                st.write(f"Data do Pedido: {pedido.get("dataPedido")}")
                if st.button("Cancelar",key=random.randint(1, 1000)):
                    cancelar_pedido(pedido["idUsuario"], pedido)
                    st.success("Pedido cancelado com sucesso!")
                    time.sleep(2)
                    st.rerun()
            preco += pedido.get("totalPedido")
    if contador == 0:
        st.write("Nenhum pedido encontrado")
    
    contador = 0
    st.header("Itens Para Aluguel:")
    for pedido in lista_aluguel:
        if pedido['idUsuario'] == st.session_state.id and pedido["status"] == status:
            contador += 1
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
                if st.button("Cancelar",key=random.randint(1, 1000)):
                    cancelar_pedido(pedido["idUsuario"], pedido)
                    st.success("Pedido cancelado com sucesso!")
                    time.sleep(2)
                    st.rerun()
            preco += aluguel.get("totalAluguel")
    if contador == 0:
        st.write("Nenhum pedido encontrado")
    return preco

def atualizar_pedido_dialog(id: int):
    lista_pedido = visualizar_pedidos()
    for pedido in lista_pedido:
        if pedido['idUsuario'] == id:
            id_pedido = pedido['idPedido']
            id_usuario = pedido["idUsuario"]
            data_pedido = pedido["dataPedido"]
            status = "Concluido"
            total_pedido = pedido["totalPedido"]
            tipo_transacao = pedido["tipoTransacao"]
            data_entrega = pedido["dataEntrega"]
            

        
            pedido_new = {
                "idUsuario": id_usuario,
                "dataPedido": data_pedido,
                "status": status,
                "totalPedido": total_pedido,
                "tipoTransacao": tipo_transacao,
                "dataEntrega": data_entrega
            }

            try:
                atualiza_pedido(id_pedido, pedido_new)
            
            except requests.exceptions.HTTPError as err:
                if err.response.status_code == 422:
                    st.error("Erro de validação: os dados enviados não estão corretos.")
                else:
                    st.error(f"Erro ao atualizar o pedido: {err}")
                st.write("Resposta da API:", err.response.text)
            
            except json.JSONDecodeError:
                st.error("Erro ao processar a resposta da API. Resposta inválida.")
            
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")
                
def encontrar_gerador(portatil:str, bateria:float, potencia:float, geradores_disponiveis:list[dict]) -> dict:
    for gerador in geradores_disponiveis:
        if (
            gerador["portatil"] == portatil and
            gerador["capacidadeBateria"] == bateria and
            gerador["potencia"] == potencia
        ):
            return gerador

    for gerador in geradores_disponiveis:
        fatores_em_comum = sum([
            gerador["portatil"] == portatil,
            gerador["capacidadeBateria"] == bateria,
            gerador["potencia"] == potencia
        ])
        if fatores_em_comum >= 2:
            return gerador

    for gerador in geradores_disponiveis:
        if (
            gerador["portatil"] == portatil or
            gerador["capacidadeBateria"] == bateria or
            gerador["potencia"] == potencia
        ):
            return gerador
    return None

def apagar_user_total(id:int):
    user = visualizar_user(id)
    for pedido in lista_pedidos:
        if pedido["idUsuario"] == id:
            for item in lista_itens:
                if item["idPedido"] == pedido["idPedido"]:
                    apagar_itens_pedido(item["idItem"])
            for aluguel in lista_alugueis:
                if aluguel["idPedido"] == pedido["idPedido"]:
                    apagar_aluguel(aluguel["idAluguel"])
            apagar_pedido(pedido["idPedido"])
    for endereco in lista_enderecos:
        if endereco["enderecoIdUser"] == user["idUsuario"]:
            apagar_endereco(endereco["idEndereco"])
    apagar_user(id)
    
