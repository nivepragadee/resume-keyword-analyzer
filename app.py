import streamlit as st
import re

# ---------- Helper Functions ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    stopwords = set([
        "the", "and", "to", "a", "of", "in", "for", "with", "on", "at", "by",
        "an", "be", "is", "are", "as", "that", "this", "it", "from", "or"
    ])
    return [word for word in words if word not in stopwords]

def extract_keywords(text):
    return set(clean_text(text))

# ---------- Streamlit App ----------
st.set_page_config(page_title="Resume Keyword Analyzer", page_icon="🧠")
st.title("🧠 Resume Keyword Analyzer")
st.write("Compare your resume against a job description to see which keywords you're missing.")

st.markdown("### 📄 Job Description")
jd_text = st.text_area("Paste the job description here", height=200)

st.markdown("### 📄 Your Resume")
resume_text = st.text_area("Paste your resume content here", height=200)

if st.button("🔍 Analyze"):
    if jd_text and resume_text:
        jd_keywords = extract_keywords(jd_text)
        resume_keywords = extract_keywords(resume_text)

        matched = jd_keywords.intersection(resume_keywords)
        missing = jd_keywords - resume_keywords
        match_percent = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0

        st.success(f"✅ Match: {len(matched)} out of {len(jd_keywords)} keywords ({match_percent:.2f}%)")
        st.markdown("### ✅ Matched Keywords")
        st.write(", ".join(sorted(matched)) if matched else "No matches found.")

        st.markdown("### ❌ Missing Keywords")
        st.write(", ".join(sorted(missing)) if missing else "No missing keywords!")

    else:
        st.warning("Please fill in both the job description and your resume.")
