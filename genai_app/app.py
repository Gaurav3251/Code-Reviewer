# # genai_app/app.py
import sys
import os

# Ensure Streamlit and Python recognize genai_app as a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from genai_app import google_client

def main():
    st.title("AI Code Reviewer")
    st.write("Submit your Python code to receive feedback on potential bugs and suggested fixes.")

    # Text area for code input.
    user_code = st.text_area("Enter your Python code below:", height=300)

    if st.button("Review Code"):
        if not user_code.strip():
            st.error("Please enter some Python code for review.")
        else:
            with st.spinner("Reviewing your code..."):
                try:
                    review_response = google_client.review_code(user_code)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    return

            # Display the response from the API.
            st.subheader("Review Response")
            st.markdown(review_response)

if __name__ == "__main__":
    main()


