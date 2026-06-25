import pandas as pd

print("Reading dataset...")

df = pd.read_csv("data/postings.csv")

print("Counting companies...")

company_count = (
    df["company_name"]
    .dropna()
    .value_counts()
    .head(20)
)

print(company_count)

company_count.to_csv(
    "output/top_companies.csv"
)

print("\nFile saved successfully!")