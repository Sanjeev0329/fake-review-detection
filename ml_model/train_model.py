import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# load cleaned data
df = pd.read_csv("./dataset/cleaned_train.csv")

# remove empty rows
df = df.dropna()

# input and output
X = df["cleaned_text"]
y = df["Label"]

# split data (train + test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# prediction
y_pred = model.predict(X_test_vec)

# accuracy
accuracy = accuracy_score(y_test, y_pred)
print("✅ Model Accuracy:", accuracy)

# save model
pickle.dump(model, open("./backend/model.pkl", "wb"))
pickle.dump(vectorizer, open("./backend/vectorizer.pkl", "wb"))

print("✅ Model and vectorizer saved successfully")