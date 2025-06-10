📖 Overview
An NLP-based application that analyzes resumes and classifies them into different job categories. This tool helps HR professionals quickly screen and filter candidates based on resume content.

🚀 Features
Preprocesses text using NLP techniques

Classifies resumes into fields like Data Science, HR, Finance, etc.

Provides top skills extracted from the resume

Clean web interface with Streamlit

🧠 Tech Stack
Python, Pandas, NumPy

NLP: NLTK, scikit-learn

Streamlit

joblib

💻 How to Run
Clone the repository:

bash
git clone https://github.com/babneek/resume-analyzer.git
Install dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py

📁 Folder Structure
resume-analyzer/
├── app.py
├── model/
│   ├── resume_model.pkl
│   └── le_skill.pkl
├── data/
│   └── updated_resume_data.csv
├── requirements.txt
