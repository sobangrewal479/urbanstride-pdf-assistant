from openai import OpenAI, AuthenticationError, RateLimitError, APIError

from src.config import OPENAI_API_KEY, OPENAI_MODEL, has_valid_openai_key
from src.fallback import get_fallback_response


SYSTEM_INSTRUCTIONS = """
You are the UrbanStride PDF Product Assistant.

You must answer using ONLY the provided PDF context.
Do not use internet knowledge.
Do not invent prices, sizes, colors, stock, policies, warranty terms, or delivery times.
If the answer is not clearly found in the PDF context, say the information is not available.
Do not give medical advice.
Keep the answer short, helpful, polite, and customer-friendly.
Mention important conditions when the PDF includes them.
"""


def build_context_from_chunks(chunks: list[dict]) -> str:
    """
    Convert retrieved chunks into one context text for the AI.
    """

    if not chunks:
        return ""

    context_parts = []

    for chunk in chunks:
        document_name = chunk.get("document_name", "Unknown document")
        chunk_text = chunk.get("chunk_text", "")

        context_parts.append(
            f"Source document: {document_name}\n"
            f"Relevant PDF text:\n{chunk_text}"
        )

    return "\n\n---\n\n".join(context_parts)


def generate_answer(question: str, relevant_chunks: list[dict]) -> str:
    """
    Generate an answer using OpenAI and only the retrieved PDF chunks.
    """

    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    if not relevant_chunks:
        return get_fallback_response(question)

    if not has_valid_openai_key():
        return (
            "OpenAI API key is not configured yet. "
            "Add your real API key in the .env file to generate AI answers."
        )

    context = build_context_from_chunks(relevant_chunks)

    client = OpenAI(api_key=OPENAI_API_KEY)

    user_prompt = f"""
User question:
{question}

PDF context:
{context}

Answer the user question using only the PDF context above.
If the answer is not clearly available in the context, say it is not available in the provided UrbanStride documents.
"""

    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_INSTRUCTIONS,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        answer = response.output_text.strip()

        if not answer:
            return get_fallback_response(question)

        return answer

    except AuthenticationError:
        return (
            "OpenAI authentication failed. Please check that your API key in the .env file is correct."
        )

    except RateLimitError:
        return (
            "OpenAI API quota or billing is not active yet. "
            "The PDF search is working, but live AI answer generation needs active API credits."
        )

    except APIError:
        return (
            "OpenAI API had a temporary problem. Please try again later."
        )

    except Exception as error:
        return (
            "AI answer generation failed safely. "
            f"Technical detail: {type(error).__name__}"
        )