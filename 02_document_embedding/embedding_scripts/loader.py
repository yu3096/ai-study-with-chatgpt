# embedding_scripts/loader.py

from pathlib import Path
from typing import List
from langchain.document_loaders import TextLoader, PyPDFLoader

def load_documents(input_dir: Path) -> List:
    documents = []
    for file_path in input_dir.glob("*"):
        if file_path.suffix == ".txt":
            loader = TextLoader(str(file_path), encoding="utf-8")
        elif file_path.suffix == ".pdf":
            loader = PyPDFLoader(str(file_path))
        else:
            print(f"❌ 지원하지 않는 파일 형식: {file_path.name}")
            continue
        documents.extend(loader.load())
    return documents