import pandas as pd
import ast


# Loading the original raw dataset
df = pd.read_csv("data/raw/gsearch_jobs.csv")

print("Original shape:", df.shape)

columns_to_remove = [ #to get rid of columns that do not provide any useful information
    "Unnamed: 0",
    "index",
    "commute_time"
]

df = df.drop(columns=columns_to_remove)

print("Cleaned shape:", df.shape)

print("\nTotal rows:", len(df))
print("Unique job IDs:", df["job_id"].nunique()) #to find the number of unique values in the column

duplicate_job_ids = df["job_id"].duplicated().sum()

print("Duplicate job IDs:", duplicate_job_ids)

duplicate_jobs = df[df["job_id"].duplicated(keep=False)] # Find rows where the job_id appears more than once

duplicate_jobs = duplicate_jobs.sort_values("job_id")

print("\nSample duplicate jobs:")
print(
    duplicate_jobs[
        ["job_id", "title", "company_name", "location", "date_time"]
    ].head(20).to_string(index=False)
)

df = df.drop_duplicates(subset="job_id", keep="first")

print("\nShape after removing duplicate jobs:", df.shape)

df["date_time"] = pd.to_datetime(df["date_time"]) # Convert date_time from text into a datetime value

print("\ndate_time data type:")
print(df["date_time"].dtype)

# Create separate date features for future analysis
df["year"] = df["date_time"].dt.year
df["month"] = df["date_time"].dt.month
df["year_month"] = df["date_time"].dt.to_period("M").astype(str)

print("\nDate sample:")
print(df[["date_time", "year", "month", "year_month"]].head())

print("\nWork from home values:")
print(df["work_from_home"].value_counts(dropna=False))


df["remote_status"] = df["work_from_home"].map({ # Create a clearer remote status column
    True: "Remote"
}).fillna("Not specified")

print("\nRemote status:")
print(df["remote_status"].value_counts())

# Clean salary columns
salary_columns = [
    "salary_avg",
    "salary_min",
    "salary_max",
    "salary_hourly",
    "salary_yearly",
    "salary_standardized"
]

for column in salary_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df["has_salary"] = df["salary_standardized"].notna()

print("\nJobs with salary information:")
print(df["has_salary"].value_counts())


# Convert skills from text into a list
df["skills"] = df["description_tokens"].apply(ast.literal_eval)

print("\nSample skills:")
print(df[["title", "skills"]].head())


# Count number of skills for each job
df["skill_count"] = df["skills"].apply(len)

print("\nSkill count sample:")
print(df[["title", "skill_count"]].head())


# Remove extra spaces from important text columns
text_columns = [
    "title",
    "company_name",
    "location",
    "schedule_type"
]

for column in text_columns:
    df[column] = df[column].str.strip()


# Final checks
print("\nFinal shape:", df.shape)
print("Duplicate job IDs:", df["job_id"].duplicated().sum())
print("Missing job IDs:", df["job_id"].isnull().sum())


# Save cleaned data
df.to_csv("data/cleaned/gsearch_jobs_cleaned.csv", index=False)

print("\nCleaned dataset saved!")