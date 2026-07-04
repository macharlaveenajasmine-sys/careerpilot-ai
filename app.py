import streamlit as st
from ui.dashboard import show_dashboard
from agents.career_manager import process_request
from tools.resume_parser import extract_text_from_pdf
from utils.pdf_generator import generate_pdf

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown("""
<div style="text-align:center;padding:20px;border-radius:15px;
background:linear-gradient(90deg,#0F62FE,#7B61FF);color:white;">

<h1>🚀 CareerPilot AI</h1>

<h3>Your AI-Powered Career Success Companion</h3>

<p>Analyze resumes • Discover skill gaps • Build roadmaps • Prepare for interviews</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("🚀 CareerPilot AI")

st.sidebar.success("🟢 AI System Online")

st.sidebar.markdown("---")

st.sidebar.subheader("🤖 AI Agents")

st.sidebar.markdown("""
✅ Resume Analyzer

✅ Skill Gap Analyzer

✅ Roadmap Planner

✅ Interview Coach

✅ Career Mentor
""")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Features")

st.sidebar.markdown("""
📄 Resume Analysis

📊 Career Dashboard

🗺 Personalized Roadmap

🎤 Interview Questions

📥 PDF Report
""")

st.sidebar.markdown("---")

st.sidebar.caption("Version 1.0")

# -------------------------------------------------
# Inputs
# -------------------------------------------------

with st.container():

    st.subheader("📋 Career Information")

    uploaded_resume = st.file_uploader(
        "📄 Upload your Resume",
        type=["pdf"]
    )

    career_goal = st.selectbox(
        "🎯 Select Career Goal",
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
        "💬 Ask a Career Question",
        placeholder="Example: How can I become an AI Engineer?"
    )
resume_status = "Yes" if uploaded_resume else "No"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🤖 **AI Agents**\n\n5 Active")

with col2:
    st.info(f"📄 **Resume Uploaded**\n\n{resume_status}")

with col3:
    st.info(f"🎯 **Career Goal**\n\n{career_goal}")

with col4:
    st.info("📥 **PDF Export**\n\nReady")

st.markdown("---")
# -------------------------------------------------
# Generate Report
# -------------------------------------------------

col1, col2, col3 = st.columns([1,2,1])

with col2:
    generate = st.button(
        "🚀 Generate AI Career Report",
        use_container_width=True
    )

if generate:

    resume_text = None

    if uploaded_resume is not None:
        resume_text = extract_text_from_pdf(uploaded_resume)

    with st.spinner("CareerPilot AI is generating your report..."):

        report = process_request(
            career_goal=career_goal,
            question=question,
            resume_text=resume_text
        )
        pdf_file = generate_pdf(report)

    st.success("AI Career Report Generated!")
    show_dashboard()

    tabs = st.tabs([
        "📄 Resume",
        "📊 Skill Gap",
        "🗺️ Roadmap",
        "🎤 Interview",
        "💡 Guidance"
    ])

    with tabs[0]:

        if "resume" in report:
            st.markdown(report["resume"])
        else:
            st.info("Upload a resume to receive resumeanalysis.")

    with tabs[1]:

        if "skill_gap" in report:
            st.markdown(report["skill_gap"])
        else:
            st.info("Upload a resume to receive skill gap analysis.")

    with tabs[2]:

        if "roadmap" in report:
            st.markdown(report["roadmap"])
        else:
            st.info("Upload a resume to receive a learning roadmap.")

    with tabs[3]:

        if "interview" in report:
            st.markdown(report["interview"])
        else:
            st.info("Upload a resume to receive interview preparation.")

    with tabs[4]:

        st.markdown(report["guidance"])
    with open(pdf_file, "rb") as file:

        st.download_button(
            label="⬇️ Download Career Report",
            data=file,
            file_name="Career_Report.pdf",
            mime="application/pdf"
        )
st.markdown("---")

st.markdown(
"""
<div style="text-align:center">

Built with ❤️ using

<b>Streamlit</b> • <b>Google Gemini</b> • <b>Python</b>

<br><br>

© 2026 CareerPilot AI

</div>
""",
unsafe_allow_html=True)
