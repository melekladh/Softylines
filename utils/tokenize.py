from nltk.tokenize import word_tokenize
import nltk
from nltk.stem.isri import ISRIStemmer
def  tokenizer  (text):
    
  
    nltk.download('punkt')
    nltk.download('punkt_tab')
    import arabicstopwords.arabicstopwords as stp
    st = ISRIStemmer()

        
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if not stp.is_stop(word)]
    return filtered_tokens  # Return list of tokens (stopwords removed)
    # return result