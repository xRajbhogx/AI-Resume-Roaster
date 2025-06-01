"""File processing utilities for PDF and text resume extraction."""

import io
import PyPDF2
import streamlit as st

def extract_text_from_pdf(file_bytes):
    """Extract text from PDF file bytes using PyPDF2."""
    reader = PyPDF2.PdfReader(file_bytes)
    # Join text from all pages, handle empty pages
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def extract_text(uploaded_file):
    """Extract text from uploaded PDF or TXT file."""
    try:
        file_type = uploaded_file.type

        # Handle PDF files
        if file_type == "application/pdf":
            with io.BytesIO(uploaded_file.read()) as file_bytes:
                return extract_text_from_pdf(file_bytes)
        
        # Handle text files
        elif file_type == "text/plain" or file_type == "application/txt":
            return uploaded_file.read().decode("utf-8")
        
        # Unsupported file type
        else:
            st.error("Unsupported file type. Please upload a PDF or TXT file.")
            return ""
            
    except Exception as e:
        # Handle file reading errors
        st.error(f"Error reading file: {e}")
        return ""

def validate_file_content(file_content):
    """Check if extracted content is not empty."""
    if not file_content.strip():
        st.error("File does not have any content.")
        st.stop()  # Stop execution if empty
        return False
    return True