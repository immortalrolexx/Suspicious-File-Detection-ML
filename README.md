<p align="center">
  <img src="https://github.com/immortalrolexx/Suspicious-File-Detection-ML/blob/main/image.png" 
       alt="Project Banner" 
       width="100%">
</p>

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Digital Forensics](https://img.shields.io/badge/Domain-Digital%20Forensics-purple)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

git clone https://github.com/immortalrolexx/Suspicious-File-Detection-ML.git
cd Suspicious-File-Detection-ML
pip install -r requirements.txt


# 🔍 Suspicious File Detection Using Machine Learning  
_A Digital Forensics Mini Project_

This project uses **Machine Learning (ML)** to classify text descriptions of file behavior or system events as either **Suspicious** (malicious) or **Safe** (benign).  
It is designed for **Digital Forensics, Cybersecurity, and Malware Analysis** scenarios.

---

## 📌 **Project Features**

✔ Uses **advanced synthetic forensic-style dataset**  
✔ Detects suspicious behaviour from **log-style textual descriptions**  
✔ ML model trained using **Random Forest Classifier**  
✔ Includes **feature extraction** using CountVectorizer  
✔ CLI-based tool to classify file behaviour in real-time  
✔ Model + vectorizer saved for reuse  
✔ Simple and effective — ideal for academic projects

---
## 🧩 Project Architecture Diagram

flowchart TD
    A[User Input: File Behaviour / Log Description] --> B[Text Preprocessing]
    B --> C[CountVectorizer]
    C --> D[Feature Vector]
    D --> E[Random Forest Classifier]
    E --> F{Prediction}
    F --> G[🔴 Suspicious File Detected]
    F --> H[🟢 Safe File Detected]

## 📁 Project Structure

```
Suspicious-File-Detection-ML/
│
├── dataset.csv              # Log-style dataset with file behaviours
│
├── model.py                 # Trains ML model (Random Forest)
├── detect.py                # CLI tool to classify suspicious/safe files
│
├── suspicious_model.pkl     # Trained Random Forest model
├── vectorizer.pkl           # Saved CountVectorizer
│
├── image.png                # Project banner
│
├── README.md                # Project documentation
│
└── venv/                    # Virtual environment (not uploaded to GitHub)
```

