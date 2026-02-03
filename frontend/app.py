import streamlit as st
import requests

st.title("📄 RAG Chatbot")

uploaded = st.file_uploader("Upload a document")
question = st.text_input("Ask a question")

if uploaded:
    upload_resp = requests.post(
        "http://localhost:8000/upload",
        files={"file": uploaded}
    ).json()

    st.success(
        f"Uploaded {upload_resp['filename']} "
        f"({upload_resp['num_chunks']} chunks)"
    )

    doc_id = upload_resp["document_id"]

if st.button("Ask") and uploaded:
    resp = requests.post(
        "http://localhost:8000/chat",
        json={
            "question": question,
            "document_id": doc_id
        }
    )

    if resp.status_code != 200:
        st.error(resp.text)
    else:
        chat_resp = resp.json()
        st.write("### Answer")
        st.write(chat_resp["answer"])
        st.write(f"Confidence: {chat_resp['confidence']:.2f}")

        with st.expander("Sources"):
            for src in chat_resp["sources"]:
                st.write(f"**{src['filename']}**")
                st.write(src["text"][:300])

