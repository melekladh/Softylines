from fastapi import FastAPI
from pydantic import BaseModel

from main import  pipeline
app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(question: str):
    print(question, "question\n\n")
    return {"answer":    pipeline(question)}

