import streamlit as st
import PyPDF2
from summarize import preprocess
from summarize import summarization
preprocess=preprocess()
summarization=summarization()
# Function to extract text from a PDF file
def extract_text_from_pdf(file):
    a=PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(a.pages)):
        page = a.pages[page_num]
        text += page.extract_text()
    return text
def sentence_formation(sentences):
    sentences=sentences.replace('\n','8055')
    sentences=sentences.replace(' ','')
    sentences=sentences.replace('8055',' ')
    sentences=sentences.split(".")
    return sentences

# Streamlit interface
st.title("PDF Summarizer")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    if st.button("Summarize"):
        with st.spinner("Extracting text..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
            sentences=sentence_formation(pdf_text)
        with st.spinner("preprocessing text..."):
            preprocess_text=preprocess.formatting(pdf_text)
            preprocess_text=preprocess.Remove_Punctuation(preprocess_text)
            preprocess_text=preprocess.convert_lower(preprocess_text)
            preprocess_text=preprocess.remove_stopwords(preprocess_text)

        with st.spinner("Summarizing text..."):
            summarize_text=summarization.summarize(preprocess_text,sentences)
        st.subheader("Summarized Text")
        st.write(summarize_text)
