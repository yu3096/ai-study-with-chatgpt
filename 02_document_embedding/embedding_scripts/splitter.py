# embedding_scripts/splitter.py

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size, chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)