import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Credentials

username = "your_username"
password = "your_password"
host = "localhost"
port = "5432"
database = "loan_analysis"

# Database Connection

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Read Cleaned CSV

df = pd.read_csv("data/cleaned_loan_data.csv")

print("Rows Loaded:", len(df))

# Load Data into PostgreSQL

df.to_sql(
    "loan_risk_data",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Data Loaded Successfully")