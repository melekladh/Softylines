from  utils.extract  import extract
from  utils.stem  import stemmer
from  utils.tokenize  import tokenizer
from utils.build_json import build
from utils.time import  extract_segments
from utils.summarize import summarize

if  __name__=="__main__":
    path = "data/audio11.mp4"
    result = extract(path)
    transcript = result["text"]                
    print ( transcript)

    
    timestamps=extract_segments(result)
    tokenized=tokenizer(transcript)
    stemmed = stemmer(tokenized)
    
    summarized=summarize(transcript)
    print (summarized )
    my_object=build(transcript,stemmed,timestamps,summarized)


    print(my_object)
