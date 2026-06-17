from src.pdf_loader import load_all_pdfs
from src.text_chunker import chunk_all_documents
from src.retriever import build_search_index, retrieve_relevant_chunks


def main():
    pdf_texts = load_all_pdfs()
    chunks = chunk_all_documents(pdf_texts)
    search_index = build_search_index(chunks)

    test_questions = [
        "How long does standard shipping take?",
        "Is UrbanWalk Pro waterproof?",
        "Which shoe is best for formal office use?",
    ]

    print("Retriever test started")
    print("-" * 40)

    for question in test_questions:
        print(f"Question: {question}")

        results = retrieve_relevant_chunks(
            question=question,
            search_index=search_index,
            top_k=2,
        )

        if not results:
            print("No relevant chunks found.")
        else:
            for result in results:
                print(f"Document: {result['document_name']}")
                print(f"Chunk ID: {result['chunk_id']}")
                print(f"Score: {result['score']}")
                print(f"Preview: {result['chunk_text'][:250]}...")
                print()

        print("-" * 40)

    print("Retriever test completed successfully")


if __name__ == "__main__":
    main()