from fastapi import FastAPI
from pydantic import BaseModel
from utils.chatmodel import load_model
from utils.embedding import load_embedding
from utils.vector import load_vector
from utils.load import load_docs
from utils.storing import store_docs
from utils.retrieval_and_gen import generate_answer
from utils.splitting import split

app = FastAPI()

llm = load_model()
embeddings = load_embedding()
vector_store = load_vector(embeddings)

docs = load_docs()
all_splits=split(docs)

store_docs(vector_store, all_splits)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(question: str):
    print(question, "question\n\n")
    return {"answer": generate_answer(vector_store, llm, question)}

