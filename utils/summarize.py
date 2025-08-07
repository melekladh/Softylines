from transformers import pipeline
def summarize (ARTICLE):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return (summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))


