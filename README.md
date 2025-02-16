# GenAI App - AI Code Reviewer

## Overview

The GenAI App is a Python application built with Streamlit that allows users to submit Python code for review. The application uses Google Generative AI to analyze the code, identify bugs or errors, suggest optimizations, and provide a corrected version of the code.

## Features

- **User-Friendly Interface:** Easily input and submit Python code.
- **AI-Powered Code Review:** Automatically review code using Google Generative AI.
- **Detailed Feedback:** Receive structured feedback, including bug identification, suggested fixes, and corrected code snippets.

## Setup Instructions

### 1. Clone the Repository
Run the following command in your terminal:

git clone <YOUR_REPOSITORY_URL>


2. Navigate into the Project Folder
Replace <repo-name> with the actual folder name created after cloning:
cd <repo-name>

3. Create and Activate a Virtual Environment
For Windows:
python -m venv venv
venv\Scripts\activate

For Mac/Linux:
python -m venv venv
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Run the Application
streamlit run genai_app/app.py

Technologies Used:
Python
Streamlit
Google Generative AI
Git & GitHub
