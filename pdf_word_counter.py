from PyPDF2 import PdfReader
import os
import time


def pdf_txt(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    file1 = open(r"1"+str(pdf[:-4])+".txt", "a+", encoding="utf-8")
    file1.writelines(text)

    file1 = open(r"1"+str(pdf[:-4])+".txt", "a+", encoding="utf-8")
    return file1


def word_count(str):
    counts = dict()
    filter = [',', '.', '-', '\'', '\"', '~', '_', '—', '“', '”', '!', '?', '’']
    for i in range(len(filter)):
        str = str.replace(filter[i], ' ')
    str = str.lower()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def listar(file):
    tempo1 = time.time()

    filename = '1'+str(file[:-4])+'.txt'
    if filename in os.listdir(os.curdir):
        try:
            txt = open(filename, 'r', encoding='cp1252').read()
        except:
            txt = open(filename, 'r', encoding='utf-8').read()
    else:
        txt = pdf_txt(file).read()
    counts = word_count(txt)
    list = (dict(sorted(counts.items(), key=lambda item: item[1])))

    print(f'Duração: {time.time() - tempo1:.2f}s')
    return list


list = listar('Dante-Alighieri-The-Divine-Comedy.pdf')
#del lista['the']
print(list)


