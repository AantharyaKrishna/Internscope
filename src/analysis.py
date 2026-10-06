import pandas as pd
import sqlite3

connection = sqlite3.connect("jobs.db")


print("\nTOP COMPANIES")

query = """
SELECT company_name, COUNT(*) AS job_count
FROM jobs
GROUP BY company_name
ORDER BY job_count DESC
LIMIT 10
"""

print(pd.read_sql_query(query, connection))


print("\nTOP LOCATIONS")

query = """
SELECT location, COUNT(*) AS job_count
FROM jobs
WHERE location IS NOT NULL
GROUP BY location
ORDER BY job_count DESC
LIMIT 10
"""

print(pd.read_sql_query(query, connection))


print("\nREMOTE STATUS")

query = """
SELECT remote_status, COUNT(*) AS job_count
FROM jobs
GROUP BY remote_status
ORDER BY job_count DESC
"""

print(pd.read_sql_query(query, connection))


print("\nAVERAGE SALARY")

query = """
SELECT AVG(salary_standardized) AS average_salary
FROM jobs
WHERE salary_standardized IS NOT NULL
"""

print(pd.read_sql_query(query, connection))


print("\nJOBS BY MONTH")

query = """
SELECT year_month, COUNT(*) AS job_count
FROM jobs
GROUP BY year_month
ORDER BY year_month
"""

print(pd.read_sql_query(query, connection))


connection.close()