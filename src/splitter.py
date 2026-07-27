from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

PDF_PATH = Path("data/documents/Press Release Page _ Press Information Bureau.pdf")

loader = PyPDFLoader(str(PDF_PATH))
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")
print(chunks[0].page_content)