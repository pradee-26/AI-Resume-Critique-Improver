import streamlit as st
from resume_utils import extract_resume_text
from ollama_client import ollama_run
from prompts import critique_prompt, rewrite_prompt
import tempfile

st.title("🧾 AI Resume Critique & Improver (Offline)")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        resume_path = tmp.name

    text = extract_resume_text(resume_path)
    st.subheader("Resume Preview")
    st.text_area("Extracted Text", text[:3000], height=250)

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing your resume..."):
            prompt = critique_prompt(text[:8000])
            feedback = ollama_run(prompt)
        st.subheader("Feedback & Suggestions")
        st.text_area("Critique", feedback, height=300)

    section_to_rewrite = st.text_area("Paste a weak section to improve:")
    if st.button("Rewrite Section"):
        with st.spinner("Rewriting..."):
            prompt = rewrite_prompt(section_to_rewrite)
            improved = ollama_run(prompt)
        st.subheader("Improved Version")
        st.text_area("Rewrite", improved, height=200)
