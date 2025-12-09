from chunker import normalize_text, chunk_text

def test_chunk_and_normalize():
    text = "This is a test text.\nWith newlines."
    norm = normalize_text(text)
    assert "newlines" in norm
    chunks = chunk_text(norm, max_words=3, overlap=1)
    assert isinstance(chunks, list)
    assert len(chunks) > 0
