from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import CHUNK_SIZE, CHUNK_OVERLAP


def create_vector_store(documents, api_key):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(api_key=api_key)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectordb
