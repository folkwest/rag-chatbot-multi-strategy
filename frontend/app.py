import streamlit as st
import requests

st.title("📄 RAG Chatbot")

uploaded = st.file_uploader("Upload a document")

chunking = st.selectbox(
    "Chunking strategy",
    ["fixed", "sentence"]
)

question = st.text_input("Ask a question")

if st.button("Ask") and uploaded:
    files = {"file": uploaded}
    upload_resp = requests.post("http://localhost:8000/upload", files=files).json()

    chat_resp = requests.post(
        "http://localhost:8000/chat",
        json={
            "question": question,
            "chunking_strategy": chunking,
            "context": upload_resp["text"]
        }
    ).json()

    st.write("### Answer")
    st.write(chat_resp["answer"])

    st.write(f"Confidence: {chat_resp['confidence']:.2f}")

    with st.expander("Sources"):
        for src in chat_resp["sources"]:
            st.write(src["text"][:300])
