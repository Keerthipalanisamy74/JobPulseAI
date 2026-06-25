import pandas as pd

df = pd.read_csv("data/postings.csv")

skills = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "aws",
    "azure",
    "machine learning"
]

results = []

text = (
    df["description"]
    .fillna("")
    .str.lower()
)

for skill in skills:
    count = text.str.contains(skill, regex=False).sum()

    results.append({
        "Skill": skill.title(),
        "Count": count
    })

skills_df = pd.DataFrame(results)

skills_df.to_csv(
    "output/top_skills.csv",
    index=False
)

print(skills_df)
print("top_skills.csv created")