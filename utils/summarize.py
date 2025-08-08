from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def summarize(text):

    tokenizer = AutoTokenizer.from_pretrained("fatmaserry/AraT5v2-arabic-summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("fatmaserry/AraT5v2-arabic-summarization")

    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)

    summary_ids = model.generate(**inputs, max_length=150, num_beams=4)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary