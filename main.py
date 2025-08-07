from  utils.extract  import extract
from  utils.stem  import stemmer
from  utils.tokenize  import tokenizer
from utils.build_json import build
from utils.time import  extract_segments
from utils.summarize import summarize

if  __name__=="__main__":
    path = "data/audio11.mp4"
    ARTICLE = 
    result = extract(path)
    transcript = result["text"]                
        
    timestamps=extract_segments(result)
    tokenized=tokenizer(transcript)
    stemmed = stemmer(tokenized)
    
    summary=summarize(ARTICLE)
    my_object=build(transcript,stemmed,timestamps)


    print(my_object)
