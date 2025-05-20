from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

# vector_db 디렉토리 경로 설정 (2단계에서 생성한 DB 사용)
VECTOR_DB_DIR = Path(__file__).resolve().parent.parent.parent /"02_document_embedding"/ "vector_db"

def retrieve_relevant_documents(query: str, top_k: int = 3):
    try:
        print(f"🔍 벡터 DB 경로: {VECTOR_DB_DIR}")
        embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        print(f"🔍 벡터 DB 로딩 중...")
        vectordb = Chroma(persist_directory=str(VECTOR_DB_DIR), embedding_function=embedder)
        print(f"🔍 벡터 DB 로딩 완료")
        
        if not VECTOR_DB_DIR.exists():
            print("❌ 벡터 DB 디렉토리가 존재하지 않습니다.")
            return []

        print(f"🔍 검색 중...")
        
        results = vectordb.similarity_search(query, k=top_k)
        print(f"🔍 검색 결과 수: {len(results)}")
        return results
    except Exception as e:
        print(f"❌ 문서 검색 중 오류 발생: {str(e)}")
        return []