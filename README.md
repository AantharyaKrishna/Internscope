# 📊 Internscope

Internscope is an interactive data analyst job market dashboard built with Python, pandas, SQL, Matplotlib, and Streamlit.

The project analyzes **58,775 unique job postings** from Google job search data to explore the skills employers are looking for, hiring trends, remote opportunities, salary information, and companies actively hiring for data-related roles.

## 🔍 Project Overview

I built Internscope to better understand the current data analyst job market and answer questions such as:

- What skills appear most frequently in data analyst job postings?
- Which companies have the most job postings?
- How has hiring activity changed over time?
- How many opportunities are explicitly listed as remote?
- What does the available salary data look like?
- Which jobs match a user's existing technical skills?

The project includes data cleaning with pandas, SQL analysis using SQLite, data visualization, and an interactive Streamlit dashboard.

## 📈 Dataset

The original dataset contains over **61,000 job-posting records** collected from Google job search results.

After investigating repeated job IDs and cleaning the dataset, the final analysis contains:

- **58,775 unique job postings**
- **13,429 companies**
- **26,379 explicitly remote postings**
- **9,686 postings with salary information**

The original dataset is not included in this repository because of its file size. A smaller dashboard-ready dataset containing only the fields required by the application is included.

**Dataset:** Data Analyst Job Postings – Google Search  
**Source:** Kaggle dataset by Luke Barousse

## 🧹 Data Cleaning

The raw dataset was explored and cleaned using pandas.

The cleaning process included:

- Removing unnecessary index and empty columns
- Investigating duplicate job IDs
- Removing repeated job postings based on `job_id`
- Converting date information into datetime format
- Creating year, month, and year-month fields for trend analysis
- Preparing salary columns for numerical analysis
- Preserving missing salary information rather than replacing it with misleading values
- Standardizing remote-work information
- Converting the dataset's existing skill-token data into Python lists for analysis
- Creating a smaller dataset specifically for the deployed dashboard

The raw dataset contained **61,953 records**, which was reduced to **58,775 unique job postings** after duplicate job IDs were removed.

## ✨ Dashboard Features

### Job Market Overview
Displays key metrics including total job postings, companies, remote jobs, and postings containing salary information.

### Most In-Demand Skills
Analyzes the existing skill-token data to identify frequently requested tools and technologies such as:

- SQL
- Excel
- Python
- Power BI
- Tableau
- R

### Top Hiring Companies
Shows the companies with the largest number of postings in the selected data.

### Hiring Trends
Visualizes how the number of records in the dataset changes over time.

### Remote Opportunities
Compares jobs explicitly identified as remote with postings where remote status was not specified.

### Salary Explorer
Analyzes available standardized salary information and displays average salary, median salary, and salary distribution.

### Skill Match
Allows users to enter skills such as:

`Python, SQL, Excel, Tableau`

Internscope then finds job postings containing one or more of those skills.

### Job Explorer
Allows users to search and explore job postings by job title, company, location, and remote status.

## 🛠️ Technologies Used

- **Python**
- **pandas**
- **NumPy**
- **SQL**
- **SQLite**
- **Matplotlib**
- **Streamlit**
- **Git & GitHub**

## 📁 Project Structure

```text
Internscope/
│
├── data/
│   └── app_jobs.csv
│
├── src/
│   ├── analysis.py
│   ├── clean_data.py
│   ├── create_app_data.py
│   ├── create_database.py
│   └── explore_data.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/AantharyaKrishna/Internscope.git
```

Move into the project:

```bash
cd Internscope
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

Then open the local Streamlit URL displayed in the terminal.

## 💡 Key Findings

Some of the strongest patterns visible in the dataset include:

- SQL is one of the most frequently requested skills for data analyst roles.
- Excel, Python, Power BI, and Tableau also appear frequently across job postings.
- A substantial number of postings explicitly offer remote work.
- Salary information is missing from many job postings, so salary analysis is performed only on postings where salary data is available.
- Skill requirements vary considerably across companies and roles, making skill-based filtering useful when exploring opportunities.

## 🎯 Project Goal

I created Internscope as a hands-on data analytics project to practice working through a complete analytics workflow:

**raw data → exploration → cleaning → transformation → SQL analysis → visualization → interactive dashboard**

The project also helped me better understand which technical skills appear most often in data analyst job postings while building a tool that can be used to explore the market interactively.

## 👤 Author

**Aantharya Krishna**

Computational Data Science student at Penn State University.