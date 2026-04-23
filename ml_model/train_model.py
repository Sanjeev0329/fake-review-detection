import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# load cleaned data
df = pd.read_csv("./dataset/cleaned_train.csv")


df = df.dropna()

# split data
X = df["cleaned_text"]
y = df["Label"]

# TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

print("Shape:", X_vectorized.shape)