from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
load_dotenv()

loader = PyPDFLoader("nodejs.pdf")
docs = loader.load()

text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_spliter.split_documents(
    documents=docs
)
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    collection_name="nodejs",
    embedding=embedding,
    url="http://localhost:6333"
)

print("indexing complete sucessfully")
