from fastapi import FastAPI
from pydantic import BaseModel
from api_server.rag_chain import generate_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000", "https://cdn.jsdelivr.net"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/chat")
async def chat(question: Question):
    answer = generate_answer(question.question)
    return {"answer": answer}
