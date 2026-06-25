import pandas as pd

print("Reading dataset...")

df = pd.read_csv("data/postings.csv")

experience_count = (
    df["formatted_experience_level"]
    .dropna()
    .value_counts()
)

print(experience_count)

experience_count.to_csv(
    "output/experience_summary.csv"
)

print("\nFile saved successfully!")