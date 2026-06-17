import streamlit as st

from src.pdf_loader import load_all_pdfs
from src.text_chunker import chunk_all_documents
from src.retriever import build_search_index, retrieve_relevant_chunks
from src.ai_answer import generate_answer


st.set_page_config(
    page_title="UrbanStride PDF Product Assistant",
    page_icon="👟",
    layout="centered",
)


@st.cache_resource
def prepare_pdf_search():
    """
    Load PDFs, extract text, create chunks, and build search index.
    Streamlit caches this so it does not repeat on every question.
    """
    pdf_texts = load_all_pdfs()
    chunks = chunk_all_documents(pdf_texts)
    search_index = build_search_index(chunks)

    return pdf_texts, chunks, search_index


st.title("UrbanStride PDF Product Assistant")
st.write(
    "Ask questions about UrbanStride product catalog, shipping, returns, warranty, sizing, and shoe care."
)

st.info(
    "This assistant answers from the provided UrbanStride PDF documents only. "
    "It does not show live inventory or private order status."
)

try:
    pdf_texts, chunks, search_index = prepare_pdf_search()

    st.success(f"Loaded {len(pdf_texts)} PDF documents successfully.")

    with st.expander("Loaded PDF documents"):
        for document_name in pdf_texts:
            st.write(f"- {document_name}")

    question = st.text_input(
        "Ask a question",
        placeholder="Example: Is UrbanWalk Pro waterproof?",
    )

    ask_button = st.button("Ask")

    if ask_button:
        if not question.strip():
            st.warning("Please type a question first.")
        else:
            with st.spinner("Searching PDFs and preparing answer..."):
                relevant_chunks = retrieve_relevant_chunks(
                    question=question,
                    search_index=search_index,
                    top_k=2,
                )

                answer = generate_answer(question, relevant_chunks)

            st.subheader("Answer")
            st.write(answer)

            st.subheader("Source reference")

            if relevant_chunks:
                for result in relevant_chunks:
                    with st.expander(
                        f"{result['document_name']} — Chunk {result['chunk_id']} — Score {result['score']}"
                    ):
                        st.write(result["chunk_text"][:1000])
            else:
                st.write("No relevant PDF source found.")

except Exception as error:
    st.error("The app could not start correctly.")
    st.write(f"Technical detail: {type(error).__name__}: {error}")