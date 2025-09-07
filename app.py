import streamlit as st
from resume_parser import parse_resume
from llm_feedback import get_feedback
from db import init_db, save_resume, fetch_resumes

# Initialize DB
init_db()

# Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Header
st.markdown("""
# 📄 AI Resume Analyzer
Analyze your resume with AI feedback, compare with job role, and store it securely.
""")

# Upload Section
with st.expander("Upload Your Resume"):
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    name = st.text_input("Enter your name:")
    job_role = st.text_input("Enter the Job Role you are targeting:")
    job_desc = st.text_area("Paste the Job Description (optional):", height=100)

    if uploaded_file is not None:
        try:
            resume_text = parse_resume(uploaded_file)
            st.success("Resume extracted successfully!")

            st.subheader("📑 Extracted Resume Text")
            st.text_area("Resume Content", resume_text, height=250)

            if st.button("Analyze & Save Resume"):
                with st.spinner("Analyzing with AI..."):
                    # Get feedback considering Job Role & Description
                    feedback = get_feedback(resume_text, job_role, job_desc)

                st.subheader("🔎 AI Feedback")
                st.markdown(feedback)

                # --- Interactive Coaching Mode ---
                st.subheader("🤝 Interactive Coaching")
                # Example missing keywords (replace with dynamic extraction later)
                missing_keywords = ["Cloud Computing", "NLP", "AWS"]  
                for kw in missing_keywords:
                    st.markdown(f"**Missing:** {kw}")
                    suggestion = f"Add a bullet point including '{kw}'"
                    st.markdown(f"**Suggestion:** {suggestion}")

                # --- Gamified ATS Score ---
                st.subheader("🎮 Resume Score Progression")
                score_before = 70
                score_after = 85
                st.progress(score_before)
                st.markdown(f"Your current score: **{score_before}%**")
                st.markdown(f"Suggested improvements can boost your score to: **{score_after}%** 🎉")

                # --- Career Roadmap Suggestions ---
                st.subheader("🚀 Career Roadmap")
                roadmap = [
                    "Since NLP is missing, consider the Coursera NLP Specialization.",
                    "Learn Cloud Computing (AWS/GCP) to improve cloud-related keywords.",
                    "Take an advanced Python or ML project to strengthen technical skills."
                ]
                for suggestion in roadmap:
                    st.markdown(f"- {suggestion}")

                # Save resume and feedback in DB
                if name.strip():
                    save_resume(name, resume_text, feedback)
                    st.success("✅ Resume and feedback saved!")

        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

# Display stored resumes
st.subheader("📂 Stored Resumes")
resumes = fetch_resumes()
if resumes:
    for rid, name, feedback in resumes:
        with st.expander(f"🗂 {name} (ID: {rid})"):
            st.markdown(f"**Feedback:**\n{feedback}")
else:
    st.info("No resumes stored yet.")
