def build(extracted ,cleaned,timestamps,summarized):
    import json

    d ={
        # "video_id": text,
        # "title": title ,
        # "duration": ,
        "timestamps": timestamps ,
        "transcription": extracted   ,
        "preprocessed_transcription" :cleaned,
        "summary" : summarized 
    }

    with open('myjson.json', 'w', encoding='utf-8') as f:

    # Convert Python dict to JSON
        obj = json.dump(d,f,ensure_ascii=False , indent=4)
        print("Converted to JSON", type(obj))
        print(obj)
    return obj 