def store_docs(vector_store,all_splits):
    vector_store.add_documents(documents=all_splits)