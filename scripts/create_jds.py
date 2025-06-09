import os

job_descriptions = [
    "Looking for a Data Scientist skilled in Python, machine learning, data visualization, and statistical modeling.",
    "Seeking a Machine Learning Engineer with experience in TensorFlow, PyTorch, and deploying ML models.",
    "Hiring an NLP Engineer with expertise in text classification, named entity recognition, and Transformers.",
    "Looking for a Backend Developer proficient in Node.js, Express, MongoDB, and REST API development.",
    "Seeking a Frontend Developer experienced in React, JavaScript, CSS, and responsive design.",
    "Hiring a Full Stack Developer with skills in React, Node.js, MongoDB, and cloud deployment.",
    "Looking for a Data Analyst proficient in SQL, Excel, Power BI, and data cleaning.",
    "Seeking an AI Researcher with strong knowledge of deep learning, reinforcement learning, and computer vision.",
    "Hiring a Software Engineer experienced in Java, object-oriented programming, and software design patterns.",
    "Looking for a DevOps Engineer skilled in Docker, Kubernetes, CI/CD pipelines, and AWS.",
    "Seeking a Cybersecurity Analyst with expertise in network security, threat detection, and incident response.",
    "Hiring a Cloud Engineer experienced in AWS, Azure, cloud architecture, and infrastructure as code.",
    "Looking for a Mobile App Developer proficient in Android development with Java/Kotlin or iOS with Swift.",
    "Seeking a Computer Vision Engineer with experience in OpenCV, image processing, and deep learning.",
    "Hiring a QA Engineer skilled in manual and automated testing, Selenium, and test case development.",
    "Looking for a Product Manager with experience in agile methodologies, user research, and roadmap planning.",
    "Seeking a Business Analyst proficient in requirement gathering, data analysis, and stakeholder communication.",
    "Hiring a Database Administrator experienced in MySQL, Oracle, backup, and recovery.",
    "Looking for a Technical Writer with strong documentation skills, API writing, and knowledge of software development.",
    "Seeking an IT Support Specialist with troubleshooting skills, hardware/software support, and customer service experience."
]

def create_jd_files(folder_path='data/job_descriptions/'):
    os.makedirs(folder_path, exist_ok=True)
    for i, jd in enumerate(job_descriptions, 1):
        filename = f'jd_{i}.txt'
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(jd)
    print(f"Created {len(job_descriptions)} job description files in '{folder_path}'.")

if __name__ == "__main__":
    create_jd_files()
