import streamlit as st
from agents.career_manager import process_request

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🚀 CareerPilot AI")
st.caption("Your Personal Multi-Agent Career Mentor")

st.markdown("---")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("CareerPilot AI")
st.sidebar.success("Project Status: Development")

# -----------------------------
# User Input
# -----------------------------
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

# -----------------------------
# Generate Response
# -----------------------------
if st.button("Generate Career Guidance"):
    if question:

        with st.spinner("CareerPilot AI is thinking..."):
            response = process_request(
                career_goal,
                question
            )

        st.success("Career Guidance Generated!")
        st.markdown(response)

    else:
        st.warning("Please enter a question.")