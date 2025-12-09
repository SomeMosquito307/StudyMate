import re

def normalize_text(s: str) -> str:
    s = s.replace('\r',' ').replace('\n',' ')
    s = re.sub(r"\s+"," ", s).strip()
    return s

def chunk_text(text: str, max_words=250, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    n = len(words)
    while i < n:
        j = min(i + max_words, n)
        chunk = ' '.join(words[i:j])
        chunks.append(chunk)
        if j == n:
            break
        i = j - overlap
    return chunks
