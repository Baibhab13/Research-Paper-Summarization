## **🔍 Visualization of LLM Explanation**

Understanding how **Large Language Models (LLMs)** work is crucial in AI research. This project provides a **visual representation** of **Transformers**, showcasing how attention mechanisms process text. Built using **Streamlit and BERTViz**, it helps users interactively explore the inner workings of LLMs.

### **🚀 Features**
- **Interactive Transformer Visualization** using BERTViz.
- **Real-time Attention Weights Analysis**.
- **User-friendly Interface** with Streamlit.
- **Custom Inputs Support** to see how different texts are processed.

---

## **📚 Text Summarization App**  

A **research paper & book summarization app** built with **Streamlit** and **Hugging Face Transformers**. This tool extracts key points from PDFs or manually inputted text, providing concise summaries in a structured format.

---

## **🚀 Setup Instructions**  

### **1️⃣ Create & Activate a Virtual Environment**  

#### **For Windows**  
```bash
python -m venv venv
venv\Scripts\activate
```

#### **For macOS & Linux**  
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **2️⃣ Install Dependencies**  
Once inside the virtual environment, install the required libraries:  

```bash
pip install -r requirements.txt
```

---

## **📌 Tech Stack**  

- **Language:** Python  
- **Libraries Used:**
  - [Streamlit](https://docs.streamlit.io/) - Web UI for user interaction  
  - [Transformers](https://huggingface.co/docs/transformers/index) - Summarization model  
  - [pdfplumber](https://pypi.org/project/pdfplumber/) - Extracting text from PDFs  
  - [re (Regex)](https://docs.python.org/3/library/re.html) - Cleaning text data  

---

## **📜 Algorithm & Code Flow**  

### **🔹 Steps Followed**  

1. **Extract Text** from PDFs using `pdfplumber`.  
2. **Filter Relevant Sections** (from **Abstract** to before **References**).  
3. **Clean the Extracted Text** (removes citations, emails, and irrelevant details).  
4. **Split into Chunks** for efficient summarization.  
5. **Summarize** the text using a pre-trained **BART Transformer model**.  
6. **Display Key Points** in a structured format.  

---

### **🔹 Code Snippet**  

```python
import streamlit as st
from transformers import pipeline
import pdfplumber
import re

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
```

---

## **🔹 How to Run the App**  

After setting up the virtual environment and installing dependencies, **start the Streamlit app**:  

```bash
streamlit run app.py
```

This will open a **web interface** where you can:  
✅ **Upload PDFs** (research papers, books, etc.)  
✅ **Manually input text**  
✅ **Get concise summaries** with key points  

---

## **💡 Use Cases**  

✔ **Researchers** - Quickly extract key findings from research papers  
✔ **Students** - Summarize academic materials for quick revision  
✔ **Professionals** - Condense lengthy reports into actionable insights  
✔ **Readers** - Get quick overviews of books and articles  

---

🔗 **Want to Contribute?** Feel free to fork the repo and improve the model! 🚀
