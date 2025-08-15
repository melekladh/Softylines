from langchain_community.document_loaders import JSONLoader

def load_docs():
   return JSONLoader(
        file_path="myjson.json",
        jq_schema=".summary",
        text_content=False,
    ).load()
