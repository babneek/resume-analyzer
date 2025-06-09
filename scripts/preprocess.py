import pandas as pd
import re
import nltk
import os
nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # remove special characters
    text = text.lower()
    tokens = text.split()
    tokens = [word for word in tokens if word not in STOPWORDS]
    return " ".join(tokens)

def load_clean_resumes(csv_path):
    df = pd.read_csv(csv_path)
    df['cleaned_resume'] = df['Resume'].apply(clean_text)
    return df[['Resume', 'cleaned_resume', 'Category']]
