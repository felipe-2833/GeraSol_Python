import streamlit as st 
from modules.utils.utils import pula_linha   


st.set_page_config(page_title="Gera Sol", page_icon="", layout="wide")

if "login" not in st.session_state:
    st.session_state["login"] = False
    
if "id" not in st.session_state:
    st.session_state["id"] = None
    
if "message_login" not in st.session_state:
    st.session_state["message_login"] = ""
    
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "carro" not in st.session_state:
    st.session_state.carro = ""
    
if "problema" not in st.session_state:
    st.session_state.problema = ""
    
if "status" not in st.session_state:
    st.session_state.status = False
    
if "lista_enderecos" not in st.session_state:
    st.session_state.lista_enderecos = []

project_name = "Gera Sol: DLS Soluções"
initial_text = (
    "O projeto Gera Sol é uma iniciativa da DLS Soluções voltada para a venda e aluguel "
    "de geradores de energia solar. Nosso objetivo é promover o uso de energia limpa, acessível "
    "e sustentável, permitindo que clientes residenciais e comerciais tenham acesso a tecnologias "
    "que reduzam custos e impactos ambientais."
)
wiz_text = (
    "A DLS Soluções é formada por Diego Bassalo Canals, Felipe Levy Stephens Fidelix e Samir Hage Neto, "
    "um grupo de estudantes comprometidos com inovação e sustentabilidade. Nosso foco está em desenvolver "
    "projetos que aliam tecnologia de ponta e impacto positivo na sociedade, proporcionando soluções práticas "
    "e eficientes."
)
objective_text = (
    "O objetivo do Gera Sol é democratizar o acesso à energia solar, oferecendo alternativas que atendam tanto "
    "às necessidades econômicas quanto ambientais de nossos clientes. Acreditamos que a energia renovável é "
    "essencial para construir um futuro mais sustentável e eficiente."
)
team = [
    "Diego Bassalo Canals",
    "Felipe Levy Stephens Fidelix",
    "Samir Hage Neto"
]

st.title(project_name)
st.write(initial_text)

st.header("Sobre Nós:")
st.write(wiz_text)

st.header("Objetivo:")
st.write(objective_text)

st.header("Equipe")
for member in team:
    st.write(member)
    