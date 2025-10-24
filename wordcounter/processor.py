import re
import pandas as pd
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def process_text(text, stop_languages=['english', 'portuguese']):
    try:
        stop_words = set()
        for lang in stop_languages:
            stop_words.update(stopwords.words(lang))
    except LookupError:
        print("Error: NLTK packages (stopwords, punkt) not found.")
        print("Please run the following commands in a Python terminal:")
        print("import nltk; nltk.download('stopwords'); nltk.download('punkt');")
        return pd.DataFrame() 

    cleaned_text = re.sub(r'[\d_]', '', text, flags=re.UNICODE)
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text, flags=re.UNICODE).lower()
    
    words = word_tokenize(cleaned_text)
    
    filtered_words = [
        word for word in words 
        if word not in stop_words and len(word) > 1
    ]
    
    word_freq = Counter(filtered_words)
    
    word_counts_df = pd.DataFrame(word_freq.items(), columns=['Words', 'Frequency'])
    word_counts_df = word_counts_df.sort_values(by='Frequency', ascending=False)
    
    return word_counts_df