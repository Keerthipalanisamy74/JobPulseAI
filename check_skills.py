import pandas as pd

df = pd.read_csv(
    "data/postings.csv"
)

print(df["skills_desc"].head(20))