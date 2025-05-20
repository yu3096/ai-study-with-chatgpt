# 03. API 챗봇 서버 구성

FastAPI 기반으로 질문을 받아 벡터 검색을 수행하고, 유사한 문서를 바탕으로 응답을 생성하는 챗봇 API를 구성합니다.

---

## ✅ 실행 방법

```bash
uvicorn api_server.main:app --reload