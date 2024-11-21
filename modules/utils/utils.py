import streamlit as st 

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
    
PROBLEMAS =  {"4":"Problemas de Motor: \n\t\t - Falhas de ignição, superaquecimento, problemas com a \n\t\tbateria ou falhas no sistema de injeção de combustível.", 
            "5":"Problemas de Transmissão: \n\t\t - Dificuldades para engatar as marchas ou ruídos \n\t\testranhos durante as mudanças.", 
            "6":"Falhas no Sistema Elétrico: \n\t\t - Falhas na bateria, alternador ou arranque.\n\t\tProblemas com sistemas de iluminação, sensores, \n\t\tsistemas de som e outros componentes eletrônicos.", 
            "7":"Problemas no Sistema de Freios: \n\t\t - Desgaste nas pastilhas ou discos de freio,\n\t\t vazamentos no sistema hidráulico, ou falhas \n\t\t no sistema de assistência de frenagem. "
        }