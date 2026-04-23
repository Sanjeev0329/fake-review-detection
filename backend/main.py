from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

# request format
class ReviewRequest(BaseModel):
    review: str

@app.get("/")
def home():
    return {"message": "Fake Review Detection API is running"}

@app.post("/predict")
def predict(data: ReviewRequest):
    review_text = data.review

    # safety check
    if not review_text.strip():
        return {
            "prediction": "Invalid input",
            "confidence": 0
        }

    # convert text
    review_vector = vectorizer.transform([review_text])

    # prediction
    prediction = model.predict(review_vector)[0]
    prob = model.predict_proba(review_vector)[0].max()

    result = "Fake" if prediction == 1 else "Real"

    return {
        "prediction": result,
        "confidence": round(float(prob), 2)
    }