# 📄 Resume Analyzer – NLP-Based Resume Classification

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resume-analyzer-3appyevanfmrqkzxfguzmrr.streamlit.app/)

**Try it online:**  
[https://resume-analyzer-3appyevanfmrqkzxfguzmrr.streamlit.app/](https://resume-analyzer-3appyevanfmrqkzxfguzmrr.streamlit.app/)

---

## 📖 Overview
An NLP-based application that analyzes resumes and classifies them into different job categories. This tool helps HR professionals quickly screen and filter candidates based on resume content.

---

## 🚀 Features
- Preprocesses text using NLP techniques
- Classifies resumes into fields like Data Science, HR, Finance, etc.
- Provides top skills extracted from the resume
- Clean web interface with Streamlit

---

## 🧠 Tech Stack
- Python
- Pandas
- NumPy
- NLP: NLTK
- scikit-learn
- Streamlit
- joblib

---

## 💻 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/babneek/resume-analyzer.git
cd resume-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`.

---

## 🧩 How to Use
1. Upload or paste your resume text in the web app.
2. Click "Analyze" to classify the resume.
3. View the job category and extracted skills.

---

## 📁 Folder Structure
```
resume-analyzer/
├── app.py
├── model/
│   ├── resume_model.pkl
│   └── le_skill.pkl
├── data/
│   └── updated_resume_data.csv
├── requirements.txt
```

---

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgements
- [Streamlit](https://streamlit.io/) for the web app framework
- [Python](https://www.python.org/) for the programming language
