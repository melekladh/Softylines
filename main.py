from  utils.extract  import extract
from  utils.stem  import stemmer
from  utils.tokenize  import tokenizer
from utils.build_json import build
from utils.time import  extract_segments
from utils.summarize import summarize
from utils.chatmodel import load_model
from utils.embedding import load_embedding
from utils.vector import load_vector
from utils.load import load_docs
from utils.storing import store_docs
from utils.retrieval_and_gen import generate_answer
from utils.splitting import split


if  __name__=="__main__":
    path = "data/audio/audio11.mp4" 
    result = extract(path)
    transcript = result["text"]                

    
    timestamps = extract_segments(result)
    tokenized = tokenizer(transcript)
    stemmed = stemmer(tokenized)
    
    summarized = summarize(transcript)
    my_object = build(transcript,stemmed,timestamps,summarized)

    llm = load_model()
    embeddings = load_embedding()
    vector_store = load_vector(embeddings)
    docs = load_docs()

    all_splits=split(docs)

    store_docs(vector_store,all_splits)

    question =  "عدد المشتركين في الهاتف القار"
    answer = generate_answer(vector_store, llm, question)
    print(answer, "test\n\n\n") 
