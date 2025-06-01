"""
AI Resume Roaster - Main Application
====================================
A Streamlit web application that uses AI to provide brutally honest, 
sarcastic feedback on resumes in Hinglish.

Author: Pushkar Shukla
Version: 0.1.0
"""

# Standard library imports
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Local module imports
from style_loader import apply_custom_styling
from file_processor import extract_text, validate_file_content
from ai_client import ResumeRoasterAI
from config import APP_TITLE, APP_CREATOR, APP_DESCRIPTION, ALLOWED_FILE_TYPES

# ============================================================================
# INITIALIZATION & CONFIGURATION
# ============================================================================

# Load environment variables from .env file
load_dotenv()

# Apply custom CSS styling to make the app look modern and attractive
apply_custom_styling()

# Configure Google's Gemini AI (optional backup AI model)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# ============================================================================
# USER INTERFACE SETUP
# ============================================================================

# Main header section
st.title(APP_TITLE)  # Display app title from config
st.divider()  # Add visual separator
st.badge(f"Made by: {APP_CREATOR}")  # Display creator badge
st.subheader(APP_DESCRIPTION)  # Display app description

#disclaimer
st.info("⚠️ **Disclaimer:** This is for learning and prototyping purposes only. AI can make mistakes - use feedback as guidance, not absolute truth!")


# Create main input section on front page with better layout
st.markdown('<div class="upload-section">', unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<h4 class="section-header">📄 Upload Your Resume</h4>', unsafe_allow_html=True)
    # File uploader widget - now in main area
    uploaded_file = st.file_uploader(
        "Choose your resume file (PDF or TXT)", 
        type=ALLOWED_FILE_TYPES,  # File types from config
        key="resume_upload",  # Unique key for session state
        help="Upload your resume in PDF or TXT format to get AI-powered roasting!"
    )

with col2:
    st.markdown('<h4 class="section-header">🎯 Target Role</h4>', unsafe_allow_html=True)
    # Text input for target job role - now in main area
    job_role = st.text_input(
        "What job are you applying for?",
        placeholder="e.g., Software Engineer, Data Scientist",
        help="Enter the job title you're targeting for more specific feedback"
    )

# Analyze button - full width below the columns
analyze = st.button("🔥 Roast My Resume!", use_container_width=True, type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# SESSION STATE MANAGEMENT
# ============================================================================

# Initialize session state for tracking uploaded files
# This prevents showing success toast on every page refresh
if "last_uploaded" not in st.session_state:
    st.session_state.last_uploaded = None

# Show success toast only when a new file is uploaded
# This prevents the toast from appearing on every interaction
if uploaded_file is not None and uploaded_file != st.session_state.last_uploaded:
    st.toast("🎉 Resume uploaded successfully!", icon="✅")
    st.session_state.last_uploaded = uploaded_file

# ============================================================================
# MAIN APPLICATION LOGIC
# ============================================================================

# Only process if user clicked analyze button AND has uploaded a file
if analyze and uploaded_file:
    try:
        # ===== FILE PROCESSING =====
        # Extract text content from uploaded file (PDF or TXT)
        file_content = extract_text(uploaded_file)
        
        # Validate that file contains actual content
        if not validate_file_content(file_content):
            st.stop()  # Halt execution if file is empty
        
        # ===== AI PROCESSING =====
        # Show spinner while AI processes the resume
        with st.spinner("🔥 AI is roasting your resume... This might sting a bit!"):
            # Initialize AI client and get roast response
            ai_client = ResumeRoasterAI()
            roast_result = ai_client.get_roast_response(file_content, job_role)
        
        # ===== RESULT DISPLAY =====
        # Display the AI's roast result to the user
        st.divider()  # Visual separator
        st.subheader("🔥 Your Resume Roast")
        
        # Create result container
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        
        try:
            # Display the AI's feedback using markdown formatting
            st.markdown(roast_result)
        except Exception as resp_error:
            # Handle any errors in displaying the result
            st.error("Unexpected error displaying the result.")
            print(f"Display error: {resp_error}")  # Log for debugging
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Add some helpful tips
        with st.expander("💡 How to use this feedback"):
            st.markdown("""
            **Remember:** 
            - The AI is trying to be funny - don't take it too personally! 😄
            - Focus on the constructive suggestions, not just the roasts
            - Use this feedback to improve your resume and try again
            - Different roles might get different feedback, so experiment!
            """)
            
    except Exception as e:
        # Catch-all error handler for unexpected issues
        st.error("An unexpected error occurred during analysis.")
        print(f"General error: {e}")  # Log for debugging

# Show helpful info if no file uploaded yet
elif analyze and not uploaded_file:
    st.warning("Please upload a resume file first! 📄")

# Show app info at the bottom
if not uploaded_file:
    st.info("👆 Upload your resume above and get ready for some brutal (but helpful) honesty!")

# ============================================================================
# END OF APPLICATION
# ============================================================================
