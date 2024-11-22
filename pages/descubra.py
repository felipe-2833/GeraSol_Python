import streamlit as st
from modules.database.catalogo import visualizar_geradores
from modules.utils.utils import encontrar_gerador

lista_geradores = visualizar_geradores()
# Configuração inicial do chatbot
init_message = (
    "Olá! Sou o assistente de escolha de geradores solares. Vamos encontrar o gerador ideal para você."
    "\nA - Sim, quero ajuda\nB - Não, obrigado\n(Digite Z para reiniciar)"
)
if not st.session_state.messages:
    st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": init_message})

# Exibindo as mensagens do chatbot
st.title("Assistente de Geradores Solares")

for message in st.session_state.messages:
    with st.chat_message(message["tipo_bot"]):
        st.markdown(message["conteudo"])

# Input do usuário
if prompt := st.chat_input("Digite aqui..."):
    match prompt.upper():
        case "A":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            response = (
                "Ótimo! Primeiro, você quer um gerador portátil?\n"
                "1 - Sim\n2 - Não\n(Digite Z para reiniciar)"
            )
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "B":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            response = "Tudo bem! Até a próxima! (Digite Z para reiniciar)"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "1":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            st.session_state.portatil = "Sim"
            response = (
                "Você prefere um gerador com capacidade de bateria?\n"
                "3040Wh - Opção 3\n4040Wh - Opção 4\n(Digite Z para reiniciar)"
            )
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "2":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            st.session_state.portatil = "Não"
            response = (
                "Você prefere um gerador com capacidade de bateria?\n"
                "3040Wh - Opção 3\n4040Wh - Opção 4\n(Digite Z para reiniciar)"
            )
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "3":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            st.session_state.bateria = "3040Wh"
            response = (
                "Você prefere uma potência de saída de?\n"
                "1800W - Opção 5\n1900W - Opção 6\n(Digite Z para reiniciar)"
            )
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "4":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            st.session_state.bateria = "4040Wh"
            response = (
                "Você prefere uma potência de saída de?\n"
                "1800W - Opção 5\n1900W - Opção 6\n(Digite Z para reiniciar)"
            )
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "5":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            st.session_state.potencia = "1800W"
            gerador = encontrar_gerador(st.session_state.portatil,st.session_state.bateria,st.session_state.potencia,lista_geradores)
            response = (
                f"Ótima escolha! Gerador portátil: {st.session_state.portatil}, "
                f"Bateria: {st.session_state.bateria}, Potência: 1800W.\n"
                f"Nos recomendamos o gerador: {gerador.get("modelo")}"
                "(Digite Z para reiniciar)"
            )
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "6":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            st.session_state.potencia = "1900W"
            gerador = encontrar_gerador(st.session_state.portatil,st.session_state.bateria,st.session_state.potencia,lista_geradores)
            response = (
                f"Ótima escolha! Gerador portátil: {st.session_state.portatil}, "
                f"Bateria: {st.session_state.bateria}, Potência: 1900W.\n"
                f"Nos recomendamos o gerador: {gerador.get("modelo")}"
                "(Digite Z para reiniciar)"
            )
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})

        case "Z":
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            with st.chat_message("assistant"):
                st.markdown(init_message)
            st.session_state.messages = [{"tipo_bot": "assistant", "conteudo": init_message}]
            st.session_state.portatil = None
            st.session_state.bateria = None
            st.session_state.potencia = None

        case _:
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})

            response = "Desculpe, não entendi. Por favor, digite uma opção válida ou Z para reiniciar."
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
            
