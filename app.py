import streamlit as st
from transformers import pipeline
import pdfplumber
import re


# Load the summarization pipeline with an optimized model for better quality
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")  # More advanced model for better summaries


summarizer = load_summarizer()


def extract_relevant_text(pdf_file):
    """Extract text from 'Abstract' to the section before 'References' in a PDF."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    match = re.search(r'(?i)abstract(.*?)(?=references|acknowledgments|bibliography)', text, re.DOTALL)
    return match.group(1) if match else text


def clean_text(text):
    """Remove references, citations, and emails from extracted text while keeping meaningful special characters."""
    text = re.sub(r'\[\d+]', '', text)  # Remove citations like [1], [2]
    text = re.sub(r'\(\d+\)', '', text)  # Remove citations in parentheses (1), (2)
    text = re.sub(r'\S+@\S+', '', text)  # Remove emails
    text = re.sub(r'\b(?:et al|ibid)\b', '', text, flags=re.IGNORECASE)  # Remove common citation phrases
    return text


# Streamlit UI
st.title("📚 Research Paper & Book Summarization App")
st.write("Upload a research paper or book (PDF) to generate a concise summary with key points.")

# Initialize session state for input persistence
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Text input box
st.session_state.user_input = st.text_area("Enter text manually (optional):", value=st.session_state.user_input,
                                           height=200)

# Clear Chat Button (Clears only user input)
if st.button("Clear Chat"):
    st.session_state.user_input = ""
    st.rerun()

# File uploader
uploaded_file = st.file_uploader("Upload a research paper or book (PDF)", type=["pdf"])

if uploaded_file is not None:
    extracted_text = extract_relevant_text(uploaded_file)
    st.session_state.user_input = clean_text(extracted_text)

# Summarization
if st.button("Summarize"):
    if st.session_state.user_input:
        with st.spinner("Summarizing document..."):
            chunk_size = 2048  # Increased chunk size for better context processing
            chunks = [st.session_state.user_input[i:i + chunk_size] for i in
                      range(0, len(st.session_state.user_input), chunk_size)]
            summaries = []
            num_chunks = len(chunks)
            max_points = min(10, num_chunks)  # Allow more points for larger content

            for chunk in chunks[:max_points]:  # Process a reasonable number of chunks
                summary = summarizer(chunk, max_length=200, min_length=80, do_sample=False)[0]['summary_text']
                summaries.append(summary)

            final_summary = "\n".join(summaries)
            key_points = final_summary.split('. ')[:max_points]  # Extract key points dynamically

            st.subheader("Key Points:")
            st.write("- " + "\n- ".join([point.strip() for point in key_points if point.strip()]))
    else:
        st.warning("Please enter text or upload a file.")
