import streamlit as st 
import json
from modules.database.catalogo import visualizar_gerador, visualizar_geradores
from modules.dialog.dialogs_catalogo import infos_gerador, comprar_gerador, alugar_gerador

lista_geradores = visualizar_geradores()
key_counter = 0


st.title("Catalogo")


for gerador in lista_geradores:
    id = gerador["idGerador"]
    with st.expander(f"{gerador["modelo"]}"):
        st.write(f"Preço Compra: {gerador.get("precoVenda")}")
        st.write(f"Preço Aluguel: {gerador.get("precoAluguelDiario")}/dia")
        key_counter += 1
        if st.button(label="Infos Gerais",key=key_counter):
            infos_gerador(id)
            
        json_data = json.dumps(gerador, indent=4)
        key_counter += 1
        st.download_button(
            label="Baixar JSON",
            data=json_data,
            file_name="dados_gerador.json",
            mime="application/json",
            key=key_counter
        )
        key_counter += 1
        if st.session_state.id == None and st.session_state.login == False:
            st.warning("Necessario realizar login para comprar ou alugar gerador.")
        else:
            if st.button(label="Comprar",key=key_counter):
                comprar_gerador(id, gerador.get("precoVenda"))
            key_counter += 1
            if st.button(label="Alugar",key=key_counter):
                alugar_gerador(id, gerador.get("precoAluguelDiario"))
            
            
            
    
    