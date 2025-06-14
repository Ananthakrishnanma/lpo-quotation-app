import streamlit as st
import fitz  # PyMuPDF
import difflib

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

st.set_page_config(page_title="LPO vs Quotation Checker")
st.title("📄 Compare Quotation & LPO PDFs")

quote_pdf = st.file_uploader("Upload Quotation PDF", type="pdf")
lpo_pdf = st.file_uploader("Upload LPO PDF", type="pdf")

if quote_pdf and lpo_pdf:
    st.info("Extracting and comparing...")
    quote_text = extract_text_from_pdf(quote_pdf)
    lpo_text = extract_text_from_pdf(lpo_pdf)

    if quote_text == lpo_text:
        st.success("✔️ Both documents match exactly.")
    else:
        diff = difflib.unified_diff(
            quote_text.splitlines(), lpo_text.splitlines(), lineterm=""
        )
        st.error("⚠️ Differences Found:")
        st.text_area("View Differences", "\n".join(diff), height=400)
