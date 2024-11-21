import streamlit as st 
from modules.utils.utils import pula_linha, PROBLEMAS

string = ""
for key,value in PROBLEMAS.items():
    string += f"\n\t {key} - {value} "

st.title("Mecânico IA:")

for message in st.session_state.messages:
    with st.chat_message(message["tipo_bot"]):
        st.markdown(message["conteudo"])
        
init = "Olá sou seu Mecanico virtual, gostaria de fazer uma consulta?\nA - Sim\n B - Não\n (digite Z para reiniciar)"
st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": init})

if prompt := st.chat_input("Digite aqui..."):
    
    match prompt.upper():
        case "A":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
        
            response = f"Certo, me informe qual carro vc gostaria de usar: \n1 - Chevrolet - Onix\n 2 - Fiat - Argo\n 3 - Chevrolet - Omega"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
        case "B":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
        
            response = f"Ok até a proxima! (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
        case "1":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            st.session_state.carro = "Chevrolet - Onix"
            response = f"Certo, agora informe o problema que está tendo: {string} \n (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
        case "2":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            st.session_state.carro = "Fiat - Argo"
            response = f"Certo, agora informe o problema que está tendo: {string} \n (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
        case "3":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            st.session_state.carro = "Chevrolet - Omega"
            response = f"Certo, agora informe o problema que está tendo: {string} \n (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
        case "4":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            st.session_state.problema = "Problemas de Motor"
            st.session_state.status = True
            response = f"Certo, agora vá a area de chamados para gerar um chamado baseado na nossa conversa. \n (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
        
        case "5":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            st.session_state.problema = "Problemas de Transmissão"
            st.session_state.status = True
            response = f"Certo, agora vá a area de chamados para gerar um chamado baseado na nossa conversa. \n (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
        
        case "6":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            st.session_state.problema = "Falhas no Sistema Elétrico"
            st.session_state.status = True
            response = f"Certo, agora vá a area de chamados para gerar um chamado baseado na nossa conversa. \n (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
        case "7":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            st.session_state.problema = "Problemas no Sistema de Freios"
            st.session_state.status = True
            response = f"Certo, agora vá a area de chamados para gerar um chamado baseado na nossa conversa. \n (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
        case "Z":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
            
            
            st.session_state.status = False
            response = init
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
            
        case _:
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
        
            response = f"Desculpe não intendi (digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
    