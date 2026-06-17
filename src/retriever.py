from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_search_index(chunks: list[dict]) -> dict:
    """
    Build a simple searchable index from text chunks.
    """

    if not chunks:
        raise ValueError("Cannot build search index because no chunks were provided.")

    chunk_texts = [chunk["chunk_text"] for chunk in chunks]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
    )

    chunk_vectors = vectorizer.fit_transform(chunk_texts)

    return {
        "chunks": chunks,
        "vectorizer": vectorizer,
        "chunk_vectors": chunk_vectors,
    }


def retrieve_relevant_chunks(
    question: str,
    search_index: dict,
    top_k: int = 3,
    min_score: float = 0.05,
) -> list[dict]:
    """
    Find the most relevant chunks for a user question.
    """

    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    vectorizer = search_index["vectorizer"]
    chunk_vectors = search_index["chunk_vectors"]
    chunks = search_index["chunks"]

    question_vector = vectorizer.transform([question])
    similarity_scores = cosine_similarity(question_vector, chunk_vectors).flatten()

    ranked_indexes = similarity_scores.argsort()[::-1]

    results = []

    for index in ranked_indexes[:top_k]:
        score = float(similarity_scores[index])

        if score >= min_score:
            chunk = chunks[index].copy()
            chunk["score"] = round(score, 4)
            results.append(chunk)

    return results