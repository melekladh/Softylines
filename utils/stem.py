
def stemmer(tokens):
    from nltk.tokenize import word_tokenize
    import nltk
    from nltk.stem.isri import ISRIStemmer
    nltk.download('punkt')
    nltk.download('punkt_tab')

    st = ISRIStemmer()
    stemmed_tokens = [st.stem(token) for token in tokens]
    return " ".join(stemmed_tokens)
        
