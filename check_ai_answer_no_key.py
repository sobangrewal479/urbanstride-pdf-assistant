from src.pdf_loader import load_all_pdfs
from src.text_chunker import chunk_all_documents
from src.retriever import build_search_index, retrieve_relevant_chunks
from src.ai_answer import generate_answer


def main():
    question = "Is UrbanWalk Pro waterproof?"

    pdf_texts = load_all_pdfs()
    chunks = chunk_all_documents(pdf_texts)
    search_index = build_search_index(chunks)

    relevant_chunks = retrieve_relevant_chunks(
        question=question,
        search_index=search_index,
        top_k=2,
    )

    answer = generate_answer(question, relevant_chunks)

    print("AI answer no-key check started")
    print("-" * 40)
    print(f"Question: {question}")
    print(f"Relevant chunks found: {len(relevant_chunks)}")
    print(f"Answer: {answer}")
    print("-" * 40)
    print("AI answer no-key check completed successfully")


if __name__ == "__main__":
    main()