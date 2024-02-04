from PyPDF2 import PdfReader
import os
import time

import matplotlib.pyplot as plt
import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')


def remove_stopwords(text):
    stop_words_en = set(stopwords.words('english'))
    stop_words_pt = set(stopwords.words('portuguese'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words_en and word.lower() not in stop_words_pt]
    return ' '.join(filtered_words)


def pdf_to_txt(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    file1 = open(str(pdf[:-4])+".txt", "a+", encoding="utf-8")
    file1.writelines(text)
    file1.close()


def word_count(txt):
    words_dict = dict()
    filter = [',', '.', '-', '\'', '\"', '~', '_', '—', '“', '”', '!', '?', '’', ':', ';', '\'\'', '``', '`', ' t ', ' s ', ' o ', ')', '(', '...', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']']
    for i in range(len(filter)):
        txt = txt.replace(filter[i], ' ')
    txt = txt.lower()
    words = txt.split()
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def pdf_word_counter():
    time1 = time.time()
    combined_txt = ''
    for filename in os.listdir('pdfs_folder'):
        if filename.endswith('.pdf'):
            pdf_to_txt(f'pdfs_folder/{filename}')
            try:    txt = open(f'pdfs_folder/{filename[:-4]}.txt', 'r', encoding='cp1252').read()
            except: txt = open(f'pdfs_folder/{filename[:-4]}.txt', 'r', encoding='utf-8').read()
            combined_txt += txt

    combined_txt = remove_stopwords(combined_txt)
    words_dict = word_count(combined_txt)
    enumerated_words = (dict(sorted(words_dict.items(), key=lambda item: item[1])))

    print(f'Elapsed time: {time.time() - time1:.2f}s')
    return enumerated_words


def clean_txt_files():
    for filename in os.listdir('pdfs_folder'):
        if filename.endswith('.pdf'):
            if os.path.exists(f'pdfs_folder/{filename[:-4]}.txt'):
                os.remove(f'pdfs_folder/{filename[:-4]}.txt')


def create_scatter_plot(data, title):
    plt.figure(figsize=(17, 6))
    plt.plot(range(len(data)), data['Frequency'], marker='o', linestyle='-', markersize=6, label='Frequency')
    plt.xticks(range(len(data)), data['Words'], rotation=90)
    plt.title(title)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


print('\nLoading...')
print('Don\'t panic.')
enumerated_words = pdf_word_counter()
print(enumerated_words)

word_counts_df = pd.DataFrame(enumerated_words.items(), columns=['Words', 'Frequency'])
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
word_counts_df = word_counts_df.sort_values(by='Frequency', ascending=False)

top_n = 100
top_words_df = word_counts_df.head(top_n)


create_scatter_plot(top_words_df, f'Top {1}-{top_n} Words')
clean_txt_files()