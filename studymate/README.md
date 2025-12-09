# StudyMate — AI-Powered Academic Assistant

StudyMate helps students extract knowledge from their study materials (PDFs, lecture notes, research papers) by generating short notes and Q&A in a conversational format.

## Features
- Upload PDFs and extract accurate text (OCR fallback for scanned pages).
- Chunk & normalize content for semantic indexing.
- Embed & store chunks using SentenceTransformers + FAISS.
- Semantic search for relevant passages.
- Generate short notes & Q/A using IBM Watsonx Mixtral-8x7B-Instruct.
- Interactive Streamlit UI.

## Setup Instructions

### 1. Clone repo & install requirements
```bash
git clone <your_repo_url> studymate
cd studymate
pip install -r requirements.txt
```

### 2. Environment variables
Create a `.env` file:
```
WATSONX_APIKEY=your_ibm_api_key
WATSONX_URL=https://api.us-south.assistant.watson.cloud.ibm.com
WATSONX_MODEL_ID=mixtral_8x7b_instruct_v01_q
```

### 3. Run locally
```bash
streamlit run app_streamlit.py
```

### 4. Run in Docker
```bash
docker build -t studymate .
docker run -p 8501:8501 studymate
```

## Tests
```bash
pytest tests/
```

## File Overview
- ingest.py → PDF → text extraction (OCR fallback).
- chunker.py → Normalize + chunk text.
- embed_and_index.py → FAISS embedding + retrieval.
- generator_watsonx.py → Calls IBM watsonx for notes & Q/A.
- app_streamlit.py → Streamlit interface.
