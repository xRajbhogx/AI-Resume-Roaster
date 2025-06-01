"""AI client for resume roasting using GitHub's GPT-4 model."""

import os
import streamlit as st
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv  # Add this import

class ResumeRoasterAI:
    """Handles AI interactions for resume analysis and roasting."""

    def __init__(self):
        """Initialize AI client with GitHub's inference endpoint."""
        # Load environment variables (crucial for Streamlit Cloud)
        load_dotenv()
        
        # GitHub AI inference configuration
        self.endpoint = "https://models.github.ai/inference"
        self.model = "openai/gpt-4o"
        
        # Try multiple ways to get the token
        self.token = (
            os.environ.get("GITHUB_TOKEN") or 
            os.getenv("GITHUB_TOKEN") or
            st.secrets.get("GITHUB_TOKEN")  # For Streamlit Cloud
        )

        # Enhanced error handling with debugging info
        if not self.token:
            st.error("🚨 API token not found!")
            st.write("**Debugging Info:**")
            st.write(f"- Environment GITHUB_TOKEN: `{bool(os.environ.get('GITHUB_TOKEN'))}`")
            st.write(f"- getenv GITHUB_TOKEN: `{bool(os.getenv('GITHUB_TOKEN'))}`")
            st.write(f"- Streamlit secrets: `{bool(st.secrets.get('GITHUB_TOKEN', None))}`")
            st.write(f"- Current working directory: `{os.getcwd()}`")
            
            # Check if running on Streamlit Cloud
            if "streamlit.io" in os.environ.get("STREAMLIT_SERVER_HEADLESS", ""):
                st.write("**Running on Streamlit Cloud - Check your app secrets!**")
                st.write("1. Go to your app dashboard")
                st.write("2. Click ⚙️ Settings → Secrets")
                st.write("3. Add: `GITHUB_TOKEN = \"your_token_here\"`")
            else:
                st.write("**Running locally - Check your .env file!**")
                st.write(f"- .env file exists: `{os.path.exists('.env')}`")
            
            st.stop()

        # Validate token format
        if not (self.token.startswith(('ghp_', 'gho_', 'ghu_', 'ghs_'))):
            st.error("🚨 Invalid GitHub token format!")
            st.write("GitHub tokens should start with `ghp_`, `gho_`, `ghu_`, or `ghs_`")
            st.stop()

        # Create Azure AI client
        try:
            self.client = ChatCompletionsClient(
                endpoint=self.endpoint,
                credential=AzureKeyCredential(self.token)
            )
        except Exception as e:
            st.error(f"Failed to initialize AI client: {e}")
            st.stop()

    def create_roast_prompt(self, file_content, job_role):
        """Create roasting prompt for AI with resume content and target role."""
        return f"""
        You are a veteran HR director with 20+ years of experience who has seen thousands of resumes. 
        Your job is to roast this resume with sharp wit and brutal honesty while providing actionable feedback.
        
        TONE: Sarcastic, witty, and unforgiving but constructive
        LANGUAGE: Mix of Hindi and English (Hinglish) - be natural and conversational
        
        ROASTING CRITERIA:
        1. Format & Design: Is it visually appealing or does it look like a 2003 Word document?
        2. Content Quality: Are achievements quantified or just generic fluff?
        3. Relevance: How well does it match the {job_role or 'target'} position?
        4. Red Flags: Typos, gaps, overused buzzwords, unrealistic claims
        5. Missing Elements: What's obviously absent that should be there?
        
        STRUCTURE YOUR ROAST:
        - Start with a brutal but funny one-liner about first impressions
        - Point out 2-3 major issues with comedic flair
        - Give 2-3 specific, actionable improvements
        - End with a reality check about their chances vs. what they need to do
        
        RESUME TO ROAST:
        {file_content}
        
        TARGET JOB ROLE: {job_role or 'Not specified'}
        
        Ignore formatting issues like weird symbols - they're from PDF conversion.
        Keep it under 500 words, sharp and memorable in Hinglish.
        Roast the resume, not the person. Be harsh on work, helpful with solutions.
        """

    def get_roast_response(self, file_content, job_role):
        """Send resume to AI and return roast response."""
        try:
            # Create prompt with resume and job role
            prompt = self.create_roast_prompt(file_content, job_role)

            # Call AI model with high creativity settings
            response = self.client.complete(
                messages=[
                    SystemMessage("You are a brutally honest, sarcastic HR expert who reviews resumes in Hinglish."),
                    UserMessage(prompt),
                ],
                temperature=1.0,  # High creativity
                top_p=1.0,        # Full token range
                model=self.model
            )

            # Return AI response content
            return response.choices[0].message.content

        except Exception as api_error:
            # Handle API errors gracefully
            st.error("Failed to get a response from the AI model. Please try again later.")
            st.write(f"**Error details:** {str(api_error)}")
            print(f"API call error: {api_error}")
            st.stop()