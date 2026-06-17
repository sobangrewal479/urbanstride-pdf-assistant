from src.pdf_loader import load_all_pdfs
from src.text_chunker import chunk_all_documents
from src.retriever import build_search_index, retrieve_relevant_chunks


def build_test_search_index():
    pdf_texts = load_all_pdfs()
    chunks = chunk_all_documents(pdf_texts)
    return build_search_index(chunks)


def test_shipping_question_retrieves_shipping_document():
    search_index = build_test_search_index()

    results = retrieve_relevant_chunks(
        question="How long does standard shipping take?",
        search_index=search_index,
        top_k=3,
    )

    assert len(results) > 0

    document_names = [result["document_name"] for result in results]

    assert "UrbanStride_Shipping_Returns_Warranty_2026.pdf" in document_names


def test_product_question_retrieves_product_or_care_document():
    search_index = build_test_search_index()

    results = retrieve_relevant_chunks(
        question="Is UrbanWalk Pro waterproof?",
        search_index=search_index,
        top_k=3,
    )

    assert len(results) > 0

    combined_text = " ".join(result["chunk_text"] for result in results)

    assert "UrbanWalk Pro" in combined_text or "not waterproof" in combined_text


def test_empty_question_raises_error():
    search_index = build_test_search_index()

    try:
        retrieve_relevant_chunks(
            question="",
            search_index=search_index,
        )
    except ValueError as error:
        assert "Question cannot be empty" in str(error)
    else:
        raise AssertionError("Expected ValueError for empty question.")