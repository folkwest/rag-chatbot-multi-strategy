import streamlit as st
import requests

st.title("📄 RAG Chatbot with Strategy Comparison")

uploaded = st.file_uploader("Upload a document")

# multi-select for strategies
chunking = st.multiselect(
    "Chunking strategies to compare",
    ["fixed", "sentence", "semantic"],
    default=["fixed"]
)

question = st.text_input("Ask a question")

doc_id = None

if uploaded:
    upload_resp = requests.post(
        "http://localhost:8000/upload",
        files={"file": uploaded}
    ).json()

    st.success(
        f"Uploaded {upload_resp['filename']}, "
        f"chunks: {upload_resp['chunks_per_strategy']}"
    )

    doc_id = upload_resp["document_id"]

if st.button("Ask") and uploaded and chunking:
    resp = requests.post(
        "http://localhost:8000/chat",
        json={
            "question": question,
            "document_id": doc_id,
            "chunking_strategy": chunking
        }
    )

    if resp.status_code != 200:
        st.error(resp.text)
    else:
        chat_resp = resp.json()
        for result in chat_resp["results"]:
            st.write(f"## Strategy: {result['strategy']}")
            st.write("**Answer:**", result["answer"])
            st.write(f"Confidence: {result['confidence']:.2f}")

            with st.expander("Sources"):
                for src in result["sources"]:
                    st.write(f"**{src['filename']} [{src['chunking_strategy']}]**")
                    st.write(src["text"][:300])
