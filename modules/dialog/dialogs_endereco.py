import streamlit as st 
import json
import time
import requests
from modules.database.enderecos import visualizar_endereco, criar_endereco, atualiza_endereco

@st.dialog("Informações de Endereço")
def infos_endereco(id: int):
    endereco = visualizar_endereco(id)  
    st.write(f"CEP: {endereco['cep']}")
    st.write(f"Rua: {endereco['rua']}")
    st.write(f"Número: {endereco['numero']}")
    st.write(f"Cidade: {endereco['cidade']}")
    st.write(f"Estado: {endereco['estado']}")
    
@st.dialog("Cadastro Novo Endereço")
def cadastrar_endereco(id: int):
    endereco_id_user = st.session_state.id
    cep = st.text_input("CEP:", placeholder="Digite o CEP")
    rua = st.text_input("Rua:", placeholder="Digite o nome da rua")
    numero = st.number_input("Número:", min_value=1, step=1)
    cidade = st.text_input("Cidade:", placeholder="Digite o nome da cidade")
    estado = st.text_input("Estado:", placeholder="Digite o estado")
    
    if not(endereco_id_user and cep and rua and numero and cidade and estado):
        st.error("Preencha todos os campos")
        
    else:
        # Botão de cadastro
        if st.button("Cadastrar Endereço"):
            endereco = {
                "enderecoIdUser": endereco_id_user,
                "cep": cep,
                "rua": rua,
                "numero": numero,
                "cidade": cidade,
                "estado": estado,
            }

            try:
                # Função para enviar o cadastro à API
                resposta_api = criar_endereco(endereco)
                st.success("Endereço cadastrado com sucesso!")
                time.sleep(2)
                st.rerun()
            except requests.exceptions.HTTPError as err:
                if err.response.status_code == 422:
                    st.error("Erro de validação: os dados enviados não estão corretos.")
                else:
                    st.error(f"Erro ao cadastrar o endereço: {err}")
                st.write("Resposta da API:", err.response.text)

            except json.JSONDecodeError:
                st.error("Erro ao processar a resposta da API. Resposta inválida.")

            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")
            
@st.dialog("Atualizar informações do endereço:")
def atualizar_endereco(id: int):
    endereco = visualizar_endereco(id)
    cep = st.text_input("CEP:", value=endereco["cep"])
    rua = st.text_input("Rua:", value=endereco["rua"])
    numero = st.number_input("Número:", value=endereco["numero"], min_value=1, step=1)
    cidade = st.text_input("Cidade:", value=endereco["cidade"])
    estado = st.text_input("Estado:", value=endereco["estado"])

    if st.button("Atualizar"):
        endereco_new = {
            "enderecoIdUser": endereco.get("enderecoIdUser"),
            "cep": cep,
            "rua": rua,
            "numero": numero,
            "cidade": cidade,
            "estado": estado,
        }

        try:
            atualiza_endereco(id, endereco_new)
            st.success("Endereço atualizado com sucesso!")
            time.sleep(2)
            st.rerun()
        
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                st.error("Erro de validação: os dados enviados não estão corretos.")
            else:
                st.error(f"Erro ao atualizar o endereço: {err}")
            st.write("Resposta da API:", err.response.text)
        
        except json.JSONDecodeError:
            st.error("Erro ao processar a resposta da API. Resposta inválida.")
        
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")