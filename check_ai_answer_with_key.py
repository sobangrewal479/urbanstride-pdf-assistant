from src.pdf_loader import load_all_pdfs
from src.text_chunker import chunk_all_documents
from src.retriever import build_search_index, retrieve_relevant_chunks
from src.ai_answer import generate_answer


def main():
    test_questions = [
        "Is UrbanWalk Pro waterproof?",
        "How long does standard shipping take?",
        "Do you sell kids shoes?",
    ]

    pdf_texts = load_all_pdfs()
    chunks = chunk_all_documents(pdf_texts)
    search_index = build_search_index(chunks)

    print("AI answer with-key check started")
    print("-" * 40)

    for question in test_questions:
        relevant_chunks = retrieve_relevant_chunks(
            question=question,
            search_index=search_index,
            top_k=2,
        )

        answer = generate_answer(question, relevant_chunks)

        print(f"Question: {question}")
        print(f"Relevant chunks found: {len(relevant_chunks)}")
        print(f"Answer: {answer}")
        print("-" * 40)

    print("AI answer with-key check completed successfully")


if __name__ == "__main__":
    main()