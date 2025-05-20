# embedding_scripts/run_embedding_pipeline.py

from embedding_scripts import config
from embedding_scripts.loader import load_documents
from embedding_scripts.splitter import split_documents
from embedding_scripts.embedder import get_embedder
from embedding_scripts.vector_store import save_to_vector_db

def main():
    print("📄 문서 로딩 중...")
    raw_docs = load_documents(config.DATA_DIR)
    print(f"🔍 로딩된 문서 수: {len(raw_docs)}")

    print("✂️ 문서 분할 중...")
    split_docs = split_documents(raw_docs, config.CHUNK_SIZE, config.CHUNK_OVERLAP)
    print(f"📄 분할된 문서 수: {len(split_docs)}")

    print("🔍 임베딩 모델 로딩 중...")
    embedder = get_embedder()

    print("💾 벡터 DB 저장 중...")
    save_to_vector_db(split_docs, embedder)

    print("🎉 임베딩 파이프라인 완료!")

if __name__ == "__main__":
    main()