import streamlit as st 
from datetime import datetime,timedelta
import requests
import json
import time
from modules.database.catalogo import visualizar_gerador, criar_pedido, visualizar_pedidos, criar_aluguel

hoje = datetime.today()
hoje_mais_dois = hoje + timedelta(days=2)

@st.dialog("Infos Gerador")
def infos_gerador(id: int):
    gerador = visualizar_gerador(id)
    st.write(f"Modelo: {gerador['modelo']}")
    st.write(f"Descrição: {gerador['descricao']}")
    st.write(f"Capacidade da Bateria: {gerador['capacidadeBateria']} Wh")
    st.write(f"Durabilidade: {gerador['durabilidade']}")
    st.write(f"Portas: {gerador['portas']}")
    st.write(f"Portátil: {gerador['portatil']}")
    st.write(f"Potência: {gerador['potencia']} W")
    st.write(f"Preço de Venda: R$ {gerador['precoVenda']:.2f}")
    st.write(f"Preço de Aluguel Diário: R$ {gerador['precoAluguelDiario']:.2f}")
    st.write(f"Tempo de Carga: {gerador['tempoCarga']}")
    
# Função de comprar gerador
@st.dialog("Comprar Gerador")
def comprar_gerador(id_gerador: int, preco_gerador:float):
    id_usuario = st.session_state.id 
    quantidade = st.number_input("Quantidade:", min_value=1, step=1)
    st.write(f"Preço Unitário: {preco_gerador}")
    preco_unitario = preco_gerador

    if st.button("Carrinho"):
        # Estrutura do pedido
        pedido = {
            "idUsuario": id_usuario,
            "dataPedido": hoje.strftime("%Y-%m-%d"),
            "status": "Pendente",
            "tipoTransacao": "Venda",
            "dataEntrega": hoje_mais_dois.strftime("%Y-%m-%d"),
            "itensPedido": [
                {
                    "idGerador": id_gerador,
                    "quantidade": quantidade,
                    "valorUnitario": preco_unitario,
                    "tipoTransacao": "Venda"
                }
            ]
        }

        try:
            resposta_api = criar_pedido(pedido)
            st.success("Pedido realizado com sucesso!")
            time.sleep(2)
            st.rerun()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                st.error("Erro de validação: os dados enviados não estão corretos.")
            else:
                st.error(f"Erro ao cadastrar pedido: {err}")
            st.write("Resposta da API:", err.response.text)

        except json.JSONDecodeError:
            st.error("Erro ao processar a resposta da API. Resposta inválida.")

        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")

# Função de alugar gerador
@st.dialog("Alugar Gerador")
def alugar_gerador(id_gerador: int, preco_aluguel: float):
    id_usuario = st.session_state.id 
    quantidade = st.number_input("Quantidade:", min_value=1, step=1)
    st.write(f"Preço Diaria: {preco_aluguel}")
    preco_unitario = preco_aluguel
    dias = st.number_input("Dias de Aluguel:", min_value=1, step=1)
    data_inicio = st.date_input("Data de Início:", min_value=hoje_mais_dois.date())
    data_fim = data_inicio + timedelta(days=dias)

    if st.button("Carrinho"):
        pedido = {
            "idUsuario": id_usuario,
            "dataPedido": hoje.strftime("%Y-%m-%d"),
            "status": "Pendente",
            "tipoTransacao": "Aluguel",
            "dataEntrega": data_inicio.strftime("%Y-%m-%d"),
            "itensPedido": [
                {
                    "idGerador": id_gerador,
                    "quantidade": quantidade,
                    "valorUnitario": preco_unitario,
                    "tipoTransacao": "Aluguel"
                }
            ]
        }

        try:
            criar_pedido(pedido)
            lista_pedidos = visualizar_pedidos()
            aluguel = {
                "dataFim": data_fim.strftime("%Y-%m-%d"),
                "dataInicio": data_inicio.strftime("%Y-%m-%d"),
                "diasAluguel": dias,
                "idGerador": id_gerador,
                "idPedido": lista_pedidos[-1].get("idPedido"),
                "idUsuario": id_usuario,
                "statusAluguel": "Ativo",
                "totalAluguel": lista_pedidos[-1].get("totalPedido") * dias,
                "valorDiario": preco_unitario
                }
            criar_aluguel(aluguel)
            st.success("Pedido realizado com sucesso!")
            time.sleep(2)
            st.rerun()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                st.error("Erro de validação: os dados enviados não estão corretos.")
            else:
                st.error(f"Erro ao cadastrar o aluguel: {err}")
            st.write("Resposta da API:", err.response.text)

        except json.JSONDecodeError:
            st.error("Erro ao processar a resposta da API. Resposta inválida.")

        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")