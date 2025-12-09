import streamlit as st
from ingest import extract_text_pages
from chunker import normalize_text, chunk_text
from embed_and_index import build_index, search
from generator_watsonx import generate_notes, generate_qa

st.title('StudyMate — PDF to Notes & Q/A')

uploaded = st.file_uploader('Upload PDF', type=['pdf'])
if uploaded:
    with open('tmp_upload.pdf','wb') as f:
        f.write(uploaded.getbuffer())
    pages = extract_text_pages('tmp_upload.pdf')
    all_chunks = []
    for p in pages:
        text = normalize_text(p['text'])
        chs = chunk_text(text)
        chs = [f"[page {p['page']}] " + c for c in chs]
        all_chunks.extend(chs)
    st.write(f'Extracted {len(pages)} pages and {len(all_chunks)} chunks')
    if st.button('Build Index'):
        build_index(all_chunks)
        st.success('Indexed')
    if st.button('Generate Notes & Q/A'):
        retrieved = search('summary', k=6)
        notes = generate_notes(retrieved)
        qa = generate_qa(retrieved)
        st.subheader('Notes')
        st.write(notes)
        st.subheader('Q/A')
        st.write(qa)

q = st.text_input('Ask an ad-hoc question')
if st.button('Answer') and q:
    retrieved = search(q, k=6)
    ans = generate_notes(retrieved)
    st.write(ans)
