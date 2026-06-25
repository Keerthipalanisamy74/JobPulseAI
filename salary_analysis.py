import pandas as pd

df = pd.read_csv("data/postings.csv")

salary = df["normalized_salary"].dropna()

print("\nSalary Statistics\n")

print("Average Salary:", salary.mean())
print("Maximum Salary:", salary.max())
print("Minimum Salary:", salary.min())

summary = pd.DataFrame({
    "Metric": [
        "Average Salary",
        "Maximum Salary",
        "Minimum Salary"
    ],
    "Value": [
        salary.mean(),
        salary.max(),
        salary.min()
    ]
})

summary.to_csv(
    "output/salary_summary.csv",
    index=False
)

print("\nFile saved successfully!")