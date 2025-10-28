# PDF Word Counter
A Python tool to analyze PDF files, count word frequency, and visualize the results. Run it as an interactive web app or as a command-line tool that exports to Excel and generates a plot.


![screenshot2](https://github.com/g-brrzzn/pdf_word_counter/assets/136928835/c72b9ca4-402f-480a-85f7-e1c7c85bb890)
![screenshot1](https://github.com/g-brrzzn/pdf_word_counter/assets/136928835/fe1168ec-e9d0-463e-ac3a-42fa04bc5326)
<img width="2558" height="1210" alt="pdfwordcounter1" src="https://github.com/user-attachments/assets/864e16d0-2d92-4891-a5bd-cc2a658651e4" />

### How to use
```console
1. Clone the repo
$ git clone https://github.com/g-brrzzn/pdf_word_counter

# 2. Change the working directory
$ cd pdf_word_counter

# 3. Install the requirements
$ python -m pip install -r requirements.txt

# 4. Download required NLTK data (one-time setup)
$ python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

# 5. Run the application (Choose one)

# --- Option 1: Run the Web App (Recommended) ---
# This will open the app in your browser.
$ streamlit run app.py

# --- Option 2: Run the Command-Line (CLI) Tool ---
# First, place the PDF files you want into the "inputs/" directory
$ python main.py
```
