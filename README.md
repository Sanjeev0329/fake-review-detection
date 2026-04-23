# 🚀 Fake Review Detection System

An AI-powered web application that detects whether a product review is **Fake or Real** using Machine Learning.

---

## 📌 Overview

Fake reviews are a major problem in e-commerce platforms.  
This project builds a complete **end-to-end system** that:

- Analyzes user input reviews  
- Classifies them using a Machine Learning model  
- Displays prediction with confidence score  
- Provides a clean and interactive UI  

---

## 🧠 Tech Stack

### 🔹 Machine Learning
- Python  
- Scikit-learn  
- TF-IDF Vectorization  
- Logistic Regression  

### 🔹 Backend
- FastAPI  
- Uvicorn  

### 🔹 Frontend
- HTML  
- CSS  
- JavaScript  

---

## 📂 Project Structure
Fake_Review_Detection/
│
├── backend/
│ ├── main.py
│ ├── model.pkl
│ └── vectorizer.pkl
│
├── frontend/
│ ├── index.html
├── ml_model/
│ ├── preprocess.py
│ └── train_model.py
│
├── dataset/ # (Not uploaded to GitHub)
├── .gitignore
└── README.md


---

## 📊 Dataset

Due to GitHub file size limits, the dataset is hosted externally:

👉 **Download Dataset:**  
https://drive.google.com/file/d/1_razOQbEfvKeyd5roquF2AmguPyvIYHS/view?usp=sharing  

### Dataset Info:
- Source: Yelp Reviews  
- Label:
  - `1` → Fake Review  
  - `-1` → Real Review  

---

## ⚙️ How It Works

### 1. Preprocessing
- Lowercasing  
- Removing stopwords  
- Cleaning text  

### 2. Feature Extraction
- TF-IDF converts text into numerical vectors  

### 3. Model Training
- Logistic Regression learns patterns in reviews  

### 4. Prediction
- Input → Vectorized → Model prediction  
- Output:
  - Fake / Real  
  - Confidence score  

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sanjeev0329/fake-review-detection.git
cd fake-review-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Download Dataset
Download from the link above
Place it inside the dataset/ folder

4️⃣ Train the Model
cd ml_model
python preprocess.py
python train_model.py

5️⃣ Run Backend
cd backend
python -m uvicorn main:app --reload

6️⃣ Run Frontend
Open frontend/index.html in your browser

🎯 Features
✅ Real-time review analysis
✅ Confidence score display
✅ Modern UI
✅ FastAPI backend
✅ End-to-end ML pipeline
⚠️ Limitations
TF-IDF does not fully understand context
May misclassify subtle fake reviews
Performance depends on dataset quality
🚀 Future Enhancements
🔹 Use BERT / Deep Learning
🔹 Add explainable AI (reason for prediction)
🔹 Chrome extension for live detection
🔹 Deploy on cloud (Render / AWS)
🔹 Multi-language support
👨‍💻 Authors
Name	Role	GitHub
Sanjeeb Yadav	Machine Learning, Backend, Integration	https://github.com/Sanjeev0329

Bhavana P	Frontend, Testing, UI Enhancements	https://github.com/Bhavanap1234
⭐ Contributing

Feel free to fork this repository and improve the project.

📌 Conclusion

This project demonstrates:

Machine Learning pipeline
Backend API integration
Frontend UI development
