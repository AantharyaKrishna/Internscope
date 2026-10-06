import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ast

st.set_page_config(
    page_title="Internscope",
    page_icon="📊",
    layout="wide"
)

# Load data
df = pd.read_csv("data/cleaned/gsearch_jobs_cleaned.csv")
df["date_time"] = pd.to_datetime(df["date_time"])

df["skills"] = df["skills"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else []
)

# Title
st.title("📊 Internscope")
st.caption(
    "Data Analyst Job Market Analytics • Skills • Salaries • Hiring Trends"
)

st.write(
    "Explore thousands of data analyst job postings to understand "
    "what employers are looking for and where opportunities are growing."
)

# Sidebar
st.sidebar.header("Filters")

remote_filter = st.sidebar.selectbox(
    "Remote Status",
    ["All", "Remote", "Not specified"]
)

company_search = st.sidebar.text_input(
    "Search Company",
    placeholder="Amazon, Google, Deloitte..."
)

location_search = st.sidebar.text_input(
    "Search Location",
    placeholder="New York, Chicago..."
)

filtered_df = df.copy()

if remote_filter != "All":
    filtered_df = filtered_df[
        filtered_df["remote_status"] == remote_filter
    ]

if company_search:
    filtered_df = filtered_df[
        filtered_df["company_name"].str.contains(
            company_search,
            case=False,
            na=False
        )
    ]

if location_search:
    filtered_df = filtered_df[
        filtered_df["location"].str.contains(
            location_search,
            case=False,
            na=False
        )
    ]

# Overview
st.header("Job Market Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Job Postings",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Companies",
    f"{filtered_df['company_name'].nunique():,}"
)

remote_jobs = (
    filtered_df["remote_status"] == "Remote"
).sum()

col3.metric(
    "Remote Jobs",
    f"{remote_jobs:,}"
)

salary_jobs = (
    filtered_df["salary_standardized"]
    .notna()
    .sum()
)

col4.metric(
    "Jobs With Salary",
    f"{salary_jobs:,}"
)

st.divider()

# Skills
st.header("Most In-Demand Skills")
st.caption("Skills appearing most frequently across the filtered job postings.")

skill_list = []

for skills in filtered_df["skills"]:
    if isinstance(skills, list):
        skill_list.extend(skills)

if skill_list:

    skill_counts = (
        pd.Series(skill_list)
        .value_counts()
        .head(15)
    )

    # Make skill names look nicer
    skill_names = {
        "sql": "SQL",
        "excel": "Excel",
        "python": "Python",
        "power_bi": "Power BI",
        "tableau": "Tableau",
        "r": "R",
        "sas": "SAS",
        "powerpoint": "PowerPoint",
        "word": "Word",
        "azure": "Azure",
        "aws": "AWS",
        "spark": "Spark",
        "snowflake": "Snowflake"
    }

    skill_counts.index = [
        skill_names.get(skill, skill.replace("_", " ").title())
        for skill in skill_counts.index
    ]

    fig, ax = plt.subplots(figsize=(10, 5))

    skill_counts.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title(
        "Top 15 Skills",
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel("Number of Job Postings")
    ax.set_ylabel("")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig)

else:
    st.info("No skill information available for these filters.")

# Companies
st.header("Top Hiring Companies")
st.caption("Companies with the most postings in the selected data.")

top_companies = (
    filtered_df["company_name"]
    .dropna()
    .value_counts()
    .head(10)
)

if len(top_companies) > 0:

    fig, ax = plt.subplots(figsize=(10, 5))

    top_companies.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_title(
        "Top 10 Hiring Companies",
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel("Number of Job Postings")
    ax.set_ylabel("")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig)

else:
    st.info("No companies found for these filters.")

# Trends
st.header("Hiring Trends Over Time")
st.caption("Number of records in the dataset by month.")

jobs_over_time = (
    filtered_df
    .groupby("year_month")
    .size()
)

if len(jobs_over_time) > 0:

    fig, ax = plt.subplots(figsize=(10, 5))

    jobs_over_time.plot(
        ax=ax,
        marker="o"
    )

    ax.set_title(
        "Job Postings by Month",
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Job Postings")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

else:
    st.info("No trend information available.")

# Remote jobs
st.header("Remote Opportunities")
st.caption(
    "Remote indicates postings explicitly marked as work-from-home. "
    "Missing values are kept as Not specified."
)

remote_counts = (
    filtered_df["remote_status"]
    .value_counts()
)

if len(remote_counts) > 0:

    fig, ax = plt.subplots(figsize=(8, 4))

    remote_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        "Remote Job Availability",
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel("")
    ax.set_ylabel("Number of Job Postings")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.xticks(rotation=0)
    plt.tight_layout()

    st.pyplot(fig)

# Salary
st.header("Salary Explorer")
st.caption(
    "Salary analysis uses only postings where standardized salary data is available."
)

salary_df = filtered_df[
    filtered_df["salary_standardized"].notna()
].copy()

if len(salary_df) > 0:

    average_salary = (
        salary_df["salary_standardized"].mean()
    )

    median_salary = (
        salary_df["salary_standardized"].median()
    )

    salary_col1, salary_col2, salary_col3 = st.columns(3)

    salary_col1.metric(
        "Average Salary",
        f"${average_salary:,.0f}"
    )

    salary_col2.metric(
        "Median Salary",
        f"${median_salary:,.0f}"
    )

    salary_col3.metric(
        "Postings With Salary",
        f"{len(salary_df):,}"
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(
        salary_df["salary_standardized"],
        bins=30
    )

    ax.set_title(
        "Salary Distribution",
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel("Standardized Salary")
    ax.set_ylabel("Number of Job Postings")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig)

else:
    st.info(
        "No salary information is available for these filters."
    )

# Skill matcher
st.header("🎯 Find Jobs That Match Your Skills")

st.write(
    "Enter skills you already know and Internscope will find "
    "postings containing those skills."
)

user_skills = st.text_input(
    "Enter your skills",
    placeholder="python, sql, excel, tableau"
)

if user_skills:

    entered_skills = [
        skill.strip().lower().replace("power bi", "power_bi")
        for skill in user_skills.split(",")
        if skill.strip()
    ]

    def calculate_match(job_skills):

        if not isinstance(job_skills, list):
            return 0

        job_skills = [
            str(skill).lower()
            for skill in job_skills
        ]

        matches = 0

        for skill in entered_skills:
            if skill in job_skills:
                matches += 1

        return matches

    matching_df = filtered_df.copy()

    matching_df["matching_skills"] = (
        matching_df["skills"]
        .apply(calculate_match)
    )

    matching_jobs = (
        matching_df[
            matching_df["matching_skills"] > 0
        ]
        .sort_values(
            "matching_skills",
            ascending=False
        )
    )

    if len(matching_jobs) > 0:

        st.success(
            f"{len(matching_jobs):,} jobs match at least one of your skills."
        )

        st.dataframe(
            matching_jobs[
                [
                    "title",
                    "company_name",
                    "location",
                    "remote_status",
                    "matching_skills"
                ]
            ].head(50),
            width="stretch"
        )

    else:
        st.warning(
            "No matching jobs found. Try entering different skills."
        )

# Job explorer
st.header("🔎 Explore Job Postings")

job_search = st.text_input(
    "Search Job Title",
    placeholder="Data Analyst, Business Analyst..."
)

job_table = filtered_df.copy()

if job_search:

    job_table = job_table[
        job_table["title"].str.contains(
            job_search,
            case=False,
            na=False
        )
    ]

st.caption(
    f"Showing {min(len(job_table), 100):,} "
    f"of {len(job_table):,} matching postings"
)

st.dataframe(
    job_table[
        [
            "title",
            "company_name",
            "location",
            "remote_status",
            "schedule_type"
        ]
    ].head(100),
    width="stretch"
)

# Footer
st.divider()

st.caption(
    "Internscope • Data Analyst Job Market Analytics • "
    "Built with Python, pandas, SQL, SQLite, Matplotlib & Streamlit"
)