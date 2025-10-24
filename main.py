import os
import time
import argparse
import matplotlib.pyplot as plt
from wordcounter.extractor import extract_text_from_pdfs
from wordcounter.processor import process_text
from wordcounter.exporter import export_to_excel, create_scatter_plot

def main(args):
    print('\nLoading...')
    print("Don't panic.")
    time1 = time.time()

    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory not found: {args.input_dir}")
        return

    print(f"Reading PDFs from '{args.input_dir}'...")
    combined_text = extract_text_from_pdfs(args.input_dir)
    
    if not combined_text:
        print("No text was extracted. Check your PDF files.")
        return

    print("Processing text and counting words...")
    stop_langs = [lang.strip() for lang in args.stop_languages.split(',')]
    word_counts_df = process_text(combined_text, stop_langs)
    
    if word_counts_df.empty:
        print("Processing failed. Please check NLTK package installation.")
        return

    print(f"Exporting total count to '{args.output_excel}'...")
    export_to_excel(word_counts_df, args.output_excel)

    print(f"Generating plot for the top {args.top_n} words...")
    top_words_df = word_counts_df.head(args.top_n)
    
    fig = create_scatter_plot(top_words_df, f'Top {args.top_n} Most Frequent Words')

    print("Displaying plot. Close the plot window to exit.")
    plt.show()

    print(f'\nDone! Total time: {time.time() - time1:.2f}s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Counts the word frequency in PDF files.")
    
    parser.add_argument('-i', '--input-dir', 
                        type=str, 
                        default='inputs/', 
                        help='Directory containing the PDF files.')
    
    parser.add_argument('-o', '--output-excel', 
                        type=str, 
                        default='word_counts.xlsx', 
                        help='Output Excel file name.')
    
    parser.add_argument('-n', '--top-n', 
                        type=int, 
                        default=100, 
                        help='Number of words to display in the plot.')
    
    parser.add_argument('-l', '--stop-languages',
                        type=str,
                        default='english,portuguese',
                        help='Stopword languages, comma-separated (e.g., "english,portuguese").')

    args = parser.parse_args()
    main(args)