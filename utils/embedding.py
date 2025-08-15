from langchain_ollama import OllamaEmbeddings

def load_embedding():
    return OllamaEmbeddings(model="llama3")