import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("UpdatedResumeDataSet.csv")

# Preprocessing function
def clean_resume(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stopwords.words('english')]
    return " ".join(text)

# Apply to dataset
df['cleaned_resume'] = df['Resume'].apply(clean_resume)
