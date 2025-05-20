from api_server.retriever import retrieve_relevant_documents

def generate_answer(question: str) -> str:
    print(f"🔍 질문: {question}")
    print(f"🔍 관련 문서 검색 중...")
    
    docs = retrieve_relevant_documents(question)
    print(f"🔍 검색된 문서 수: {len(docs)}")
    if not docs:
        print(f"❌ 관련 문서 검색 실패")
        return "죄송해요, 관련된 정보를 찾을 수 없어요."

    # 가장 관련 있는 문서 1개만 간단히 반환
    top_doc = docs[0].page_content.strip()
    return f"📚 참고 정보: {top_doc}"
