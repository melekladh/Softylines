from langchain import hub

def generate_answer(vector_store ,llm ,question):
    prompt = hub.pull("rlm/rag-prompt")

    retrieved_docs = vector_store.similarity_search(question, k=2)
    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

    prompt_value = prompt.invoke({"question": question, "context": docs_content })
    return llm.invoke(prompt_value)
 