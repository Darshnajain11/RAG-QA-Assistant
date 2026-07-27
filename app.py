import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(page_title="RAG PDF Assistant", page_icon="📄")

st.title("RAG Assistant")
st.write("Ask questions about the uploaded Press Information Bureau document.")

@st.cache_resource
def load_components():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    return retriever, llm

retriever, llm = load_components()

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a helpful AI assistant.

Use ONLY the information provided in the context.

If the answer is not available in the context, reply exactly:

"I couldn't find this information in the provided document."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)