from src.pdf_loader import load_all_pdfs
from src.text_chunker import chunk_all_documents


def main():
    pdf_texts = load_all_pdfs()
    chunks = chunk_all_documents(pdf_texts)

    print("Text chunking test started")
    print("-" * 40)
    print(f"Total documents loaded: {len(pdf_texts)}")
    print(f"Total chunks created: {len(chunks)}")
    print("-" * 40)

    for chunk in chunks[:5]:
        print(f"Document: {chunk['document_name']}")
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(f"Preview: {chunk['chunk_text'][:150]}...")
        print()

    print("-" * 40)
    print("Text chunking test completed successfully")


if __name__ == "__main__":
    main()