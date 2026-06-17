from src.pdf_loader import load_all_pdfs


def main():
    pdf_texts = load_all_pdfs()

    print("PDF loading test started")
    print("-" * 40)

    for document_name, text in pdf_texts.items():
        print(f"Loaded: {document_name}")
        print(f"Characters extracted: {len(text)}")
        print()

    print("-" * 40)
    print("PDF loading test completed successfully")


if __name__ == "__main__":
    main()