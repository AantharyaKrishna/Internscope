import pandas as pd
import numpy as np

df=pd.read_csv("data/raw/gsearch_jobs.csv") #loading the dataset 

print(df.head()) #displaying first 5 rows

print("\nDataset size:")
print(df.shape) #returns the number of rows and columns 

print("\nColumn Names:")
for column in df.columns: #for loop that prints the name of every column that exists
    print (column)

print("\nDataset Info:")
print(df.info()) #returns the col name, data type and values that aren't missing(non-null)

print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False)) #displays the column with the most missign values

print("\nMissing value percentages:")

missing_percent = (df.isnull().sum() / len(df)) * 100

print(missing_percent.sort_values(ascending=False))

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nSample values from selected columns:")

columns_to_check = [
    "Unnamed: 0",
    "index",
    "via",
    "extensions",
    "thumbnail",
    "search_term",
    "search_location",
    "work_from_home",
    "salary",
    "salary_pay",
    "salary_rate"
]

for column in columns_to_check:
    print(f"\n--- {column} ---")
    print(df[column].head())