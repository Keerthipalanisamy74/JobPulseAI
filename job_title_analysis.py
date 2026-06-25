import pandas as pd

df = pd.read_csv("data/postings.csv")

title_count = (
    df["title"]
    .dropna()
    .value_counts()
    .head(20)
)

print(title_count)

title_count.to_csv(
    "output/top_job_titles.csv"
)

print("\nFile saved successfully!")