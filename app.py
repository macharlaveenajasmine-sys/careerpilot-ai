import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key not found!")
    st.stop()

client = genai.Client(api_key=api_key)

# -----------------------------
# Page Settings
# -----------------------------
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.caption("Your Personal Multi-Agent Career Mentor")

st.markdown("---")

st.sidebar.title("CareerPilot AI")
st.sidebar.success("Project Status: Development")

career_goal = st.selectbox(
    "Choose your career goal",
    [
        "Artificial Intelligence",
        "Cybersecurity",
        "Data Science",
        "Software Development",
        "Cloud Computing",
        "UI/UX Design"
    ]
)

question = st.text_area(
    "Ask CareerPilot AI",
    placeholder="Example: I'm a B.Tech CSE student. Create a roadmap to become an AI Engineer."
)

if st.button("Generate Career Guidance"):
    if question:

        prompt = f"""
        The user's career goal is {career_goal}.

        User Question:
        {question}

        Give:
        1. Career Advice
        2. Skills Required
        3. Learning Resources
        4. Suggested Projects
        5. Interview Preparation Tips
        """

        with st.spinner("CareerPilot AI is thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success("Career Guidance Generated!")

        st.markdown(response.text)