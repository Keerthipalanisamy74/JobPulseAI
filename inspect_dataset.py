import pandas as pd

print("Reading dataset...")

df = pd.read_csv(
    "data/postings.csv",
    nrows=5
)

print("\nFirst 5 rows:\n")

print(df.head())

print("\nColumns:\n")

print(df.columns.tolist())