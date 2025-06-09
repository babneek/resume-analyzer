import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import load_clean_resumes

# Load resumes
resume_df = load_clean_resumes('data/resume/UpdatedResumeDataSet.csv')
resumes = resume_df['cleaned_resume'].tolist()

# Load job descriptions
jd_dir = 'data/job_descriptions/'
jd_texts = []
jd_names = []

for filename in os.listdir(jd_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(jd_dir, filename), 'r', encoding='utf-8') as f:
            jd_texts.append(f.read())
            jd_names.append(filename)

# Combine corpus
corpus = resumes + jd_texts
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

resume_vectors = X[:len(resumes)]
jd_vectors = X[len(resumes):]

# Calculate similarity scores
similarity = cosine_similarity(jd_vectors, resume_vectors)

# Print top matches
for i, jd_name in enumerate(jd_names):
    print(f"\nTop matches for JD: {jd_name}")
    top_n = similarity[i].argsort()[-5:][::-1]
    for idx in top_n:
        print(f"→ Score: {similarity[i][idx]:.2f} | Category: {resume_df.iloc[idx]['Category']}")
