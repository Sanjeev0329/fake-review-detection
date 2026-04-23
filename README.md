🚀 Fake Review Detection System

An AI-powered web application that detects whether a product review is Fake or Real using Machine Learning.

📌 Overview

Fake reviews are a major problem in e-commerce platforms. This project aims to solve that by building an end-to-end system that:

Analyzes user input reviews
Uses ML model to classify them
Displays prediction with confidence score
Provides a clean and interactive UI
🧠 Tech Stack
🔹 Machine Learning
Python
Scikit-learn
TF-IDF Vectorization
Logistic Regression
🔹 Backend
FastAPI
Uvicorn
🔹 Frontend
HTML
CSS
JavaScript
📂 Project Structure
Fake_Review_Detection/
│
├── backend/              # FastAPI backend
│   ├── main.py
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── frontend/             # Website UI
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── ml_model/             # ML training pipeline
│   ├── dataset.py
│   ├── preprocess.py
│   └── train_model.py
│
├── dataset/              # (Ignored in GitHub)
│
├── .gitignore
└── README.md
📊 Dataset

Due to GitHub file size limitations, the dataset is hosted on Google Drive:

👉 Download here:
🔗 https://drive.google.com/file/d/1_razOQbEfvKeyd5roquF2AmguPyvIYHS/view?usp=sharing

Dataset Details:
Source: Yelp Reviews
Contains labeled reviews
Label:
1 → Fake Review
-1 → Real Review
⚙️ How It Works
1. Preprocessing
Lowercasing
Removing stopwords
Cleaning text
2. Feature Extraction
TF-IDF converts text into numerical vectors
3. Model Training
Logistic Regression learns patterns from reviews
4. Prediction
User input → Vectorized → Model prediction
Output:
Fake / Real
Confidence score
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/fake-review-detection.git
cd fake-review-detection
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Download Dataset
Download from the Google Drive link
Place it inside the dataset/ folder
4️⃣ Train the Model
cd ml_model
python preprocess.py
python train_model.py
5️⃣ Run Backend
cd backend
python -m uvicorn main:app --reload
6️⃣ Run Frontend
Open frontend/index.html in browser
🌐 API Endpoint
POST /predict

Request:

{
  "review": "This product is amazing!"
}

Response:

{
  "prediction": "Fake",
  "confidence": 0.89
}
🎯 Features
✅ Real-time review analysis
✅ Confidence score visualization
✅ Clean and modern UI
✅ FastAPI backend
✅ End-to-end ML pipeline
⚠️ Limitations
Model uses TF-IDF → limited understanding of context
May misclassify subtle fake reviews
Depends heavily on dataset quality
🚀 Future Enhancements
🔹 Use Deep Learning (BERT / Transformers)
🔹 Add Explainable AI (why review is fake)
🔹 Chrome Extension for real-time detection
🔹 Deploy on cloud (Render / AWS)
🔹 Multi-language support
## 👨‍💻 Authors

- **Sanjeeb Yadav** – Machine Learning, Backend (FastAPI), System Integration  
  🔗 https://github.com/Sanjeev0329  

- **Bhavana P** – Frontend Development, Testing, UI Enhancements  
  🔗 https://github.com/Bhavanap1234  

Computer Science Student
Passionate about AI & Mobile App Development
⭐ Contribute

Feel free to fork the repo and improve the project!

📌 Final Note

This project demonstrates:

Machine Learning pipeline
Backend API integration
Frontend UI development

👉 Making it a complete full-stack AI project
