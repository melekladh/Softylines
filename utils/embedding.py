from langchain_huggingface import HuggingFaceEmbeddings

def load_embedding():

    embeddings = HuggingFaceEmbeddings(model_name="Omartificial-Intelligence-Space/GATE-AraBert-v1")
    return embeddings