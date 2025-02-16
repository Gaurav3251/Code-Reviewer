# genai_app/google_client.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompt import SYSTEM_PROMPT

# Load environment variables from .env file
load_dotenv()

def review_code(code: str) -> str:
    """
    Uses Google Generative AI to review Python code.
    It returns a text response containing:
      - Bug/Error Identification
      - Suggested Fixes/Optimizations
      - Corrected Code

    The API key must be stored in the environment variable 'GOOGLE_API_KEY'.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise Exception("Google API key not set. Please set the 'GOOGLE_API_KEY' environment variable.")

    # Configure the Google Generative AI client with your API key.
    genai.configure(api_key=api_key)

    try:
        # Initialize the model
        model = genai.GenerativeModel("gemini-pro") 
        response = model.generate_content(SYSTEM_PROMPT + "\n\n" + code)

        # Extract and return the response text
        return response.text

    except Exception as e:
        raise Exception(f"Error calling Google Generative AI API: {e}")


