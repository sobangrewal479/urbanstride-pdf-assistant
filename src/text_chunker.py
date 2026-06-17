def chunk_text(
    text: str,
    document_name: str,
    chunk_size: int = 900,
    overlap: int = 150,
) -> list[dict]:
    """
    Split long PDF text into smaller searchable chunks.
    """

    if not text or not text.strip():
        raise ValueError("Cannot chunk empty text.")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0.")

    if overlap < 0:
        raise ValueError("overlap cannot be negative.")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size.")

    chunks = []
    start = 0
    chunk_id = 1
    text = text.strip()

    while start < len(text):
        end = start + chunk_size
        chunk_text_value = text[start:end].strip()

        if chunk_text_value:
            chunks.append(
                {
                    "document_name": document_name,
                    "chunk_id": chunk_id,
                    "chunk_text": chunk_text_value,
                }
            )

        chunk_id += 1
        start = end - overlap

    return chunks


def chunk_all_documents(
    pdf_texts: dict[str, str],
    chunk_size: int = 900,
    overlap: int = 150,
) -> list[dict]:
    """
    Split all loaded PDF documents into chunks.
    """

    all_chunks = []

    for document_name, text in pdf_texts.items():
        document_chunks = chunk_text(
            text=text,
            document_name=document_name,
            chunk_size=chunk_size,
            overlap=overlap,
        )
        all_chunks.extend(document_chunks)

    return all_chunks