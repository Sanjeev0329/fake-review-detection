import pandas as pd
import nltk
import re
from nltk.corpus import stopwords

nltk.download('stopwords')

# load dataset
df = pd.read_csv("./dataset/Labelled_Yelp_Dataset.csv")

# select columns
df = df[["Review", "Label"]]

# convert labels: -1 → 1 (Fake), 1 → 0 (Real)
df["Label"] = df["Label"].apply(lambda x: 1 if x == -1 else 0)

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# apply cleaning
df["cleaned_text"] = df["Review"].apply(clean_text)

# final dataset
df = df[["cleaned_text", "Label"]]

print(df.head())

# save cleaned dataset
df.to_csv("./dataset/cleaned_train.csv", index=False)

print("✅ Preprocessing Completed")