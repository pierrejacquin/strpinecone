import streamlit as st
import pinecone
from pinecone import Pinecone, ServerlessSpec

# Define a versão esperada para compatibilidade com o plugin
pinecone.__version__ = "6.0.1"

from pinecone_plugins.assistant.models.chat import Message

# Inicializa o Pinecone com sua API key e especificação do ambiente
pc = Pinecone(
    api_key="pcsk_aQPmV_8aQxJeJc2hNi68pHUUoAqmZ75hR7kRhRyyWBsgxGfoUBjpA26vJ6hEuP7dwGnq5",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)

# Cria o assistente
assistant = pc.assistant.Assistant(assistant_name="expertinhoemimposto")

# Cria a interface com Streamlit
st.title("Interface do Assistente Pinecone")

# Campo de entrada para a pergunta do usuário
user_input = st.text_input("Digite sua pergunta:")

# Quando o usuário clicar no botão 'Enviar' e houver uma pergunta
if st.button("Enviar") and user_input:
    # Cria a mensagem do usuário
    msg = Message(role="user", content=user_input)
    # Envia a mensagem e recebe a resposta
    resp = assistant.chat(messages=[msg])
    # Exibe apenas o conteúdo da resposta
    st.subheader("Resposta do Assistente")
    st.write(resp.message.content)
