# 02. 문서 임베딩 및 벡터 DB 저장

이 단계에서는 `.txt` 또는 `.pdf` 문서를 벡터로 임베딩하고,
Chroma 벡터 DB에 저장하는 파이프라인을 구성합니다.

---

## ✅ 폴더 구조

- `embedding_scripts/`: 임베딩 파이프라인 코드
- `data/`: 문서를 넣는 폴더
- `vector_db/`: 임베딩된 벡터들이 저장될 DB (실행 후 생성됨)

---

## ⚙️ 실행 방법

```bash
# 문서 임베딩 파이프라인 실행
python -m embedding_scripts.run_embedding_pipeline