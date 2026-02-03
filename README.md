# RAG Chatbot with Multi-Strategy Chunking

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-%2300BAFF?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black?style=for-the-badge&logo=openai&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-vector%20store-lightgrey)


This is a **Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload documents (PDF/TXT), select different **chunking strategies**, and ask questions about the content. The system supports **multi-document storage**, **confidence scoring**, and **strategy comparison** (fixed, sentence, semantic chunking).


![Demo](assets/demo_gif_rag_chatbot.gif)

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the project](#running-the-project)
- [How to use](#how-to-use)
- [Notes](#notes)
- [Next Improvements](#next-improvements)
- [License](#license)


---

## Features

- Upload **multiple documents** and store them in a vector database (FAISS)
- Automatic **text chunking** strategies:
  - `fixed` – fixed word-length chunks
  - `sentence` – sentence-based chunks
  - `semantic` – semantic chunks with smaller overlapping word windows
- **Strategy comparison mode**: ask the same question across multiple chunking strategies to see which performs best
- **Confidence scores** for answers
- **Sources** returned for transparency
- **Streamlit frontend** for easy interaction

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rag-chatbot-v2.git
cd rag-chatbot-v2
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Add your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

---

## Running the project
1. Starting the backend (FastAPI)
```bash
uvicorn backend.main:app --reload
```
2. Starting the frontend (Streamlit)
```bash
streamlit run frontend/app.py
```

---

## How to use

- Upload a document (PDF or TXT) in the Streamlit UI.

- Select chunking strategies to compare (`fixed`, `sentence`, `semantic`).

- Ask a question about the document.

- View answers per strategy, confidence scores, and source chunks.

- Repeat with multiple documents to compare strategies or combine knowledge.

---

## Notes
- Semantic chunking now uses **smaller, overlapping word windows** for better retrieval.

- Confidence scores are calculated based on distance in the vector store.

- All document chunks are stored in-memory via FAISS for fast retrieval.

- Multi-document support is built-in - you can query one document at a time or extend to multiple.

---

## Next Improvements
- Persist FAISS vector store to disk for long-term storage

- Add side-by-side UI comparison cards

- Enhance semantic chunking using embedding clustering

---

## License
MIT License
Feel free to use and modify!
