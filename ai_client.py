"""AI client for resume roasting using GitHub's GPT-4 model."""

import os
import streamlit as st
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

class ResumeRoasterAI:
    """Handles AI interactions for resume analysis and roasting."""

    def __init__(self):
        """Initialize AI client with GitHub's inference endpoint."""
        # GitHub AI inference configuration
        self.endpoint = "https://models.github.ai/inference"
        self.model = "openai/gpt-4o"
        self.token = os.environ.get("GITHUB_TOKEN")

        # Validate API token exists
        if not self.token:
            st.error("API token not found. Please check your environment variables.")
            st.stop()

        # Create Azure AI client
        self.client = ChatCompletionsClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.token)
        )

    def create_roast_prompt(self, file_content, job_role):
        """Create roasting prompt for AI with resume content and target role."""
        return f"""
        You are an experienced HR professional with a knack for delivering brutally honest yet constructive feedback on resumes.
        Your responses are sharp, witty, and insightful, blending humor with actionable advice to help candidates improve their resumes.

        PERSONA: Imagine you're a mix of Simon Cowell's bluntness, Mindy Kaling's humor, and a seasoned HR expert who has seen it all.

        TONE: Sarcastic, clever, and brutally honest, but always constructive and professional. Use humor to make your points memorable.

        ROASTING CRITERIA:
        1. First Impressions: Does the resume grab attention or make you want to look away? Is it visually appealing or outdated?
        2. Format & Design: Is it clean, professional, and easy to navigate, or cluttered and confusing?
        3. Content Quality: Are achievements clearly quantified and impactful, or vague and unimpressive?
        4. Relevance: Does it align with the {job_role} position, or does it feel like a generic template?
        5. Red Flags: Typos, inconsistencies, overused buzzwords, or unrealistic claims.
        6. Missing Elements: Are there critical sections or details missing that would make the resume stronger?

        STRUCTURE YOUR RESPONSE:
        - Start with a witty one-liner summarizing your first impression of the resume.
        - Highlight 2-3 major issues with specific examples from the resume, using humor to make your points memorable.
        - Provide 2-3 actionable suggestions for improvement, keeping the advice sharp and practical.
        - End with a motivational note or reality check, balancing humor with encouragement.

        RESUME TO REVIEW:
        {file_content}
    ignore some formatting issues like weird symbols or lines as they are comming because of the pdf to text conversion.
        TARGET JOB ROLE:
        Keep your response concise, under 500 words,give answer in hindi+english(hinglish) and ensure it is both entertaining and helpful. Focus on roasting the resume constructively while maintaining a professional tone.
        """

    def get_roast_response(self, file_content, job_role):
        """Send resume to AI and return roast response."""
        try:
            # Create prompt with resume and job role
            prompt = self.create_roast_prompt(file_content, job_role)

            # Call AI model with high creativity settings
            response = self.client.complete(
                messages=[
                    SystemMessage("You are a brutally honest, sarcastic HR expert who reviews resumes."),
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
            print(f"API call error: {api_error}")
            st.stop()