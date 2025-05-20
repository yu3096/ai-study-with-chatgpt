# embedding_scripts/vector_store.py

from langchain_community.vectorstores import Chroma
from embedding_scripts.config import VECTOR_DB_DIR

def save_to_vector_db(docs, embedder):
    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embedder,
        persist_directory=str(VECTOR_DB_DIR)
    )
    vectordb.persist()
    print("✅ Vector DB 저장 완료!")