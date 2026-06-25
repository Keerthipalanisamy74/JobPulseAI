import pandas as pd

print("Reading dataset...")

df = pd.read_csv("data/postings.csv")

print("Counting locations...")

location_count = (
    df["location"]
    .value_counts()
    .head(20)
)

print(location_count)

location_count.to_csv(
    "output/top_locations.csv"
)

print("\nFile saved successfully!")