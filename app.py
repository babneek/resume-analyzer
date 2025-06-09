import streamlit as st
import os
import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    tokens = text.split()
    tokens = [w for w in tokens if w not in STOPWORDS]
    return " ".join(tokens)

@st.cache_data(show_spinner=False)
def load_job_descriptions(jd_folder='data/job_descriptions/'):
    jds = []
    jd_names = []
    for file in os.listdir(jd_folder):
        if file.endswith('.txt'):
            path = os.path.join(jd_folder, file)
            with open(path, 'r', encoding='utf-8') as f:
                jd_names.append(file)
                jds.append(f.read())
    return jd_names, jds

def main():
    st.title("NLP-Powered Resume Screening Tool")
    st.write("Upload a resume (txt) to see matching job descriptions.")

    uploaded_file = st.file_uploader("Upload Resume Text File", type=["txt"])
    if uploaded_file is not None:
        resume_text = uploaded_file.read().decode("utf-8")
        st.subheader("Uploaded Resume:")
        st.write(resume_text)

        # Clean resume text
        cleaned_resume = clean_text(resume_text)

        # Load JDs
        jd_names, jd_texts = load_job_descriptions()

        # Vectorize
        vectorizer = TfidfVectorizer()
        corpus = [cleaned_resume] + jd_texts
        X = vectorizer.fit_transform(corpus)

        resume_vec = X[0]
        jd_vecs = X[1:]

        # Compute similarity
        similarity_scores = cosine_similarity(resume_vec, jd_vecs)[0]

        # Get top 5 matches
        top_indices = similarity_scores.argsort()[-5:][::-1]

        st.subheader("Top Matching Job Descriptions:")
        for idx in top_indices:
            st.markdown(f"**{jd_names[idx]}** - Similarity Score: {similarity_scores[idx]:.2f}")
            st.write(jd_texts[idx])
            st.markdown("---")

if __name__ == "__main__":
    main()
