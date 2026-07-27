from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
PDF_PATH = Path("data/documents/Press Release Page _ Press Information Bureau.pdf")
loader = PyPDFLoader(str(PDF_PATH))
documents = loader.load()
print(f"Total Pages Loaded: {len(documents)}")
print(documents[0].page_content)