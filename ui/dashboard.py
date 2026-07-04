import streamlit as st


def show_dashboard():

    st.subheader("📊 Career Readiness Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Overall Readiness",
            "82%",
            "+12%"
        )

        st.progress(0.82)

        st.metric(
            "Resume Quality",
            "90%"
        )

        st.progress(0.90)

        st.metric(
            "Projects",
            "70%"
        )

        st.progress(0.70)

    with col2:

        st.metric(
            "Technical Skills",
            "85%"
        )

        st.progress(0.85)

        st.metric(
            "Interview Readiness",
            "75%"
        )

        st.progress(0.75)

        st.metric(
            "Communication",
            "80%"
        )

        st.progress(0.80)