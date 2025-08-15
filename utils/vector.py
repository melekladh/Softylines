from langchain_core.vectorstores import InMemoryVectorStore

def load_vector(embeddings):
    return InMemoryVectorStore(embeddings)
