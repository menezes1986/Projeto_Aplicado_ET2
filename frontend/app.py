import streamlit as st
import requests
import json

#LOGICA DO FORNTEND DO PROJETO FEITA POR MAÚRICIO VIANA

st.image('frontend\WhatsApp Image 2025-03-31 at 17.31.41.jpeg', width=300)
st.title("Comparador de Documentos via API Google Sheets")

token_url = "http://localhost:8000/token"
compare_url = "http://localhost:8001/comparar"
#campos de input str dos arquivos
st.markdown("<h3 style='color: #FF5733;'>Nome da Planilha SEFAZ</h3>", unsafe_allow_html=True)
nome_sefaz = st.text_input("Digite o nome da Planilha SEFAZ", key="input_sefaz")

st.markdown("<h3 style='color: #FF5733;'>Nome da Planilha SISTEMA</h3>", unsafe_allow_html=True)
nome_sistema = st.text_input("Digite o nome da Planilha SISTEMA", key="input_sistema")

#BOTÃO COMPARAR...
st.markdown(
    """
    <style>
        .stButton > button {
            background-color: #007BFF; /* Azul */
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Comparar", key="comparar_button"):
    try:
        token_resp = requests.post(token_url)
        token = token_resp.json().get("access_token")
        headers = {"Authorization": f"Bearer {token}"}
        params = {"sefaz": nome_sefaz, "sistema": nome_sistema}
        resposta = requests.post(compare_url, json=params, headers=headers)

        if resposta.status_code == 200:
            print(resposta.json())
            st.success("Diferença encontrada")
            st.dataframe(resposta.json()["diferença"])
        else:
            st.error(f"Erro: {resposta.text}")
    except Exception as e:
        st.error(f"Erro: {e}")

#CUSTOMIZAÇÃO DO PROJETO FEITA POR ESTHEFANE RAELY