from langchain_text_splitters import RecursiveCharacterTextSplitter

def split (docs):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,  
        chunk_overlap=50, 
        add_start_index=True,  
    )
    print(f"Split blog post into {len(text_splitter.split_documents(docs))} sub-documents.")

    return text_splitter.split_documents(docs)

