from ingest import extract_text_pages

def test_pdf_extraction():
    pages = extract_text_pages('sample_data/sample.pdf')
    assert isinstance(pages, list)
    assert 'text' in pages[0]
