import pandas as pd

df = pd.read_csv("./dataset/Labelled_Yelp_Dataset.csv")

print("Columns:", df.columns)
print(df.head())
print("Shape:", df.shape)