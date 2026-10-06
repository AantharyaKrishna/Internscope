import pandas as pd

df = pd.read_csv("data/cleaned/gsearch_jobs_cleaned.csv")

columns = [
    "title",
    "company_name",
    "location",
    "schedule_type",
    "salary_standardized",
    "remote_status",
    "year_month",
    "skills"
]

app_df = df[columns].copy()

app_df.to_csv("data/app_jobs.csv", index=False)

print("App dataset created!")
print("Rows:", len(app_df))