# 🚀 Loan Risk Analysis Dashboard

An End-to-End Data Analytics Project built using Python, PostgreSQL, SQL, and Power BI.

---

# 📑 Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Dataset Information](#dataset-information)
- [Data Pipeline](#data-pipeline)
- [Python ETL Process](#python-etl-process)
- [PostgreSQL Database Design](#postgresql-database-design)
- [SQL Analysis](#sql-analysis)
- [Power BI Dashboard](#power-bi-dashboard)
- [Dashboard Screenshots](#dashboard-screenshots)
- [Key Insights](#key-insights)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

# Project Overview

This project analyzes loan application data to identify patterns affecting loan approvals and customer risk profiles.

The project demonstrates a complete Data Analytics workflow:

CSV Dataset → Python ETL → PostgreSQL → SQL Analysis → Power BI Dashboard → Business Insights

The objective is to help financial institutions understand:

- Loan approval trends
- Credit risk levels
- Customer demographics
- Default behavior
- Income and education impacts

---

# Business Problem

Financial institutions receive thousands of loan applications.

Approving risky customers can increase default rates while rejecting good customers can reduce revenue.

The goal of this project is to:

- Identify low-risk applicants
- Understand approval patterns
- Analyze credit score behavior
- Study previous default impact
- Generate actionable business insights

---

# Project Architecture

```text
CSV Dataset
      │
      ▼
Python Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
PostgreSQL Database
      │
      ▼
SQL Business Analysis
      │
      ▼
Power BI Dashboard
      │
      ▼
Business Insights
```

---

# Tech Stack

### Programming

- Python
- SQL

### Libraries

- Pandas
- NumPy
- SQLAlchemy
- Psycopg2

### Database

- PostgreSQL

### Visualization

- Power BI

### Version Control

- Git
- GitHub

---

# Dataset Information

Dataset contains:

- 45,000 Loan Applications

Important Features:

- Age
- Income
- Education
- Home Ownership
- Loan Amount
- Interest Rate
- Credit Score
- Previous Defaults
- Loan Intent
- Loan Status

Target Variable:

- Loan Approval Status

---

# Data Pipeline

The complete workflow followed:

1. Raw CSV Data Collection
2. Data Cleaning using Python
3. Feature Engineering
4. PostgreSQL Data Loading
5. SQL Analysis
6. Power BI Dashboard Creation
7. Business Insight Generation

---

# Python ETL Process

Python was used to:

### Data Cleaning

- Handle missing values
- Remove duplicates
- Standardize column names
- Convert data types

### Feature Engineering

Created:

- Age Group
- Income Category
- Credit Category
- Risk Category

### Data Loading

Data loaded automatically into PostgreSQL using SQLAlchemy.

---

# PostgreSQL Database Design

Database Name:

```sql
loan_analysis
```

Main Table:

```sql
loan_risk_data
```

Data loaded from Python directly into PostgreSQL.

Example Query:

```sql
SELECT COUNT(*)
FROM loan_risk_data;
```

Output:

```text
45000
```

---

# SQL Analysis

Business Questions Answered:

### Total Applications

```sql
SELECT COUNT(*)
FROM loan_risk_data;
```

### Approval Rate

```sql
SELECT
AVG(loan_status)*100
FROM loan_risk_data;
```

### Credit Score Analysis

```sql
SELECT
MIN(credit_score),
MAX(credit_score),
AVG(credit_score)
FROM loan_risk_data;
```

### Loan Intent Analysis

```sql
SELECT
loan_intent,
COUNT(*)
FROM loan_risk_data
GROUP BY loan_intent;
```

---

# Power BI Dashboard

The dashboard contains three pages:

## 1. Executive Overview

KPIs:

- Total Applications
- Approved Loans
- Rejected Loans
- Approval Rate
- Average Loan Amount
- Average Credit Score

Visuals:

- Approval Distribution
- Education Analysis
- Loan Intent Analysis

---

## 2. Customer Analysis

Visuals:

- Age Distribution
- Gender Distribution
- Income Analysis
- Education Analysis
- Home Ownership Analysis

Filters:

- Gender
- Age Group
- Income Category
- Education

---

## 3. Risk Analysis

Visuals:

- Credit Category Distribution
- Risk Category Distribution
- Loan Amount vs Credit Score
- Previous Default Analysis

KPIs:

- Avg Credit Score
- High Risk Applicants
- Low Risk Applicants

---

# Dashboard Screenshots

## Executive Overview

Add Screenshot Here

```text
screenshots/executive_overview.png
```

---

## Customer Analysis

Add Screenshot Here

```text
screenshots/customer_analysis.png
```

---

## Risk Analysis

Add Screenshot Here

```text
screenshots/risk_analysis.png
```

---

# Key Insights

### Insight 1

Customers with higher credit scores have a significantly higher approval probability.

### Insight 2

Low-risk applicants contribute to the majority of approved loans.

### Insight 3

Previous defaults negatively affect loan approval decisions.

### Insight 4

Income and education levels influence borrowing behavior.

### Insight 5

Most applications are submitted for Education and Medical purposes.

---

# Project Structure

```text
Loan-Risk-Analysis/
│
├── data/
│   └── loan_data.csv
│
├── scripts/
│   ├── cleaning.py
│   ├── load_data.py
│   └── db_connection.py
│
├── sql/
│   └── analysis_queries.sql
│
├── dashboard/
│   └── Loan_Risk_Analysis.pbix
│
├── screenshots/
│   ├── executive_overview.png
│   ├── customer_analysis.png
│   └── risk_analysis.png
│
└── README.md
```

---

# Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/Loan-Risk-Analysis.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Script

```bash
python scripts/load_data.py
```

### Open Dashboard

```text
dashboard/Loan_Risk_Analysis.pbix
```

---

# Future Improvements

- Machine Learning Loan Prediction Model
- Automated ETL Scheduling
- Power BI Service Deployment
- Real-Time Loan Monitoring Dashboard
- Customer Segmentation Models

---

# Author

### Abhishek Chaudhary

Data Analyst | Python | SQL | PostgreSQL | Power BI

EMail:
(abhi14chaudhary@gmail.com)

LinkedIn:
(www.linkedin.com/in/abhishek-chaudhary-py)

GitHub:
(https://github.com/dark-code77)

---
⭐ If you found this project useful, consider giving it a star.

Thanks for Visit...