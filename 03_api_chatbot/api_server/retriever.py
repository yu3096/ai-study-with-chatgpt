from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path


# vector_db 디렉토리 경로 설정 (2단계에서 생성한 DB 사용)
VECTOR_DB_DIR = Path(__file__).resolve().parent.parent.parent /"02_document_embedding"/ "vector_db"

def retrieve_relevant_documents(query: str, top_k: int = 3):
    try:
        print(f"🔍 벡터 DB 경로: {VECTOR_DB_DIR}")
        embedder = HuggingFaceEmbeddings(model_name="snunlp/KR-SBERT-V40K-klueNLI-augSTS")
        print(f"🔍 벡터 DB 로딩 중...")
        
        # FAISS 벡터 DB 로드
        vectordb = FAISS.load_local(str(VECTOR_DB_DIR)
                                        , embedder
                                        , allow_dangerous_deserialization=True) # 해당 옵션은 보안 이슈가 있기 때문에 사용하지 않는 것이 좋음
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