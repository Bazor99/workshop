import streamlit as st
import tempfile

from components.file_loader import load_pdf, extract_text
from components.vector_store import create_vector_store
from components.retriever import retrieve_context
from components.llm_engine import analyze_resume
from components.report_generator import generate_markdown_report


st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🚀 AI Resume Analyzer")

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")


jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")
cv_file = st.file_uploader("Upload CV (PDF)", type="pdf")

if st.button("Analyze"):

    if not api_key or not jd_file or not cv_file:
        st.error("Please provide all required inputs.")
        st.stop()

    with st.spinner("Processing..."):

        # Save temp files
        with tempfile.NamedTemporaryFile(delete=False) as tmp_jd:
            tmp_jd.write(jd_file.read())
            jd_path = tmp_jd.name

        with tempfile.NamedTemporaryFile(delete=False) as tmp_cv:
            tmp_cv.write(cv_file.read())
            cv_path = tmp_cv.name

        # Load & process
        jd_pages = load_pdf(jd_path)
        cv_pages = load_pdf(cv_path)

        cv_text = extract_text(cv_pages)

        vectordb = create_vector_store(jd_pages, api_key)

        context = retrieve_context(vectordb)

        analysis = analyze_resume(context, cv_text, api_key)

        report = generate_markdown_report(analysis)

    st.success("Analysis Complete!")

    st.metric("ATS Score", f"{analysis['match_score']}/100")

    st.download_button(
        "Download Report",
        report,
        file_name="resume_analysis_report.md"
    )
    st.markdown(report)