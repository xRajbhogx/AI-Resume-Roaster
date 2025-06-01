"""CSS style loading utilities for Streamlit app customization."""

import streamlit as st
import os

css_file = 'styles.css'  # Default CSS file name

def load_css(file_name):
    """Load CSS from file and inject into Streamlit app."""
    try:
        # Check if CSS file exists
        if not os.path.exists(file_name):
            st.error(f"CSS file '{file_name}' not found.")
            return
            
        # Read CSS content and inject into app
        with open(file_name, 'r', encoding='utf-8') as f:
            css_content = f.read()
            st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
            
    except UnicodeDecodeError:
        # Handle encoding errors
        st.error(f"Error reading CSS file '{file_name}'. Check file encoding.")
    except Exception as e:
        # Handle other file errors
        st.error(f"Error loading CSS: {str(e)}")

def apply_custom_styling():
    """Apply default custom styling from styles.css file."""
    load_css('styles.css')