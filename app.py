import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from io import BytesIO

from wordcounter.processor import process_text
from wordcounter.exporter import create_scatter_plot

def main():
    st.set_page_config(layout="wide", page_title="PDF Word Counter")
    st.title("PDF Word Counter 📊")

    with st.sidebar:
        st.header("Settings")
        
        uploaded_files = st.file_uploader(
            "Upload your PDF files", 
            type="pdf", 
            accept_multiple_files=True
        )
        
        top_n = st.number_input(
            "Top N words to plot", 
            min_value=5, 
            max_value=200, 
            value=50
        )
        
        stop_langs_input = st.text_input(
            "Stopword languages (comma-separated)", 
            value="english,portuguese"
        )
        
        analyze_button = st.button("Analyze PDFs")

    if analyze_button and uploaded_files:
        combined_text = ""

        with st.spinner(f"Reading {len(uploaded_files)} PDF(s)..."):
            for file in uploaded_files:
                try:
                    reader = PdfReader(file)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            combined_text += text + "\n"
                except Exception as e:
                    st.error(f"Error reading '{file.name}': {e}")

        if combined_text:
            with st.spinner("Processing text and counting words..."):
                stop_langs = [lang.strip() for lang in stop_langs_input.split(',')]
                word_counts_df = process_text(combined_text, stop_langs)
            
            st.success("Analysis complete!")

            top_words_df = word_counts_df.head(top_n)

            st.header(f"Top {top_n} Most Frequent Words")
            
            fig = create_scatter_plot(top_words_df, f'Top {top_n} Words')
            st.pyplot(fig)

            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                word_counts_df.to_excel(writer, index=False, sheet_name='WordCounts')
            
            st.download_button(
                label="📥 Download Full Report (Excel)",
                data=output.getvalue(),
                file_name="pdf_word_count_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            st.header("Full Word Count Data")
            st.dataframe(word_counts_df)

    elif analyze_button and not uploaded_files:
        st.warning("Please upload at least one PDF file.")
    
    else:
        st.info("Upload PDF files and click 'Analyze' to see the results.")

if __name__ == "__main__":
    main()