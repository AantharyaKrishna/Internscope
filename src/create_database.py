import pandas as pd
import sqlite3

df = pd.read_csv("data/cleaned/gsearch_jobs_cleaned.csv")

connection = sqlite3.connect("jobs.db")

df.to_sql(
    "jobs",
    connection,
    if_exists="replace",
    index=False
)

print("Database created!")

query = """
SELECT COUNT(*) AS total_jobs
FROM jobs
"""

result = pd.read_sql_query(query, connection)

print(result)

connection.close()