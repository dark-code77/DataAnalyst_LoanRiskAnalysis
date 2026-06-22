import pandas as pd
import numpy as np

df=pd.read_csv("data/loan_data.csv")
print(df.shape)

percent_cols = [
    "person_income",
    "person_emp_exp",
    "loan_amnt",
    "loan_int_rate",
    "loan_percent_income",
    "cb_person_cred_hist_length",
    "loan_status"
]
for col in percent_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("%","")
        .astype(float)
        /100
    )

# Age Group 
    df["age_group"] = pd.cut(
    df["person_age"],
    bins=[18,25,35,45,100],
    labels=["Young","Adult","Middle Age","Senior"]
)
    
# Income Category
    df["income_category"] = pd.qcut(
    df["person_income"],
    q=3,
    labels=[
        "Low Income",
        "Medium Income",
        "High Income"
    ]
)

# Credit Category

    df["credit_category"] = pd.cut(
    df["credit_score"],
    bins=[300,580,670,740,900],
    labels=[
        "Poor",
        "Fair",
        "Good",
        "Excellent"
    ]
)
    
# Risk Category 

    conditions = [
    (df["credit_score"] < 580),
    (df["credit_score"].between(580,700)),
    (df["credit_score"] > 700)
]

choices = [
    "High Risk",
    "Medium Risk",
    "Low Risk"
]

df["risk_category"] = np.select(
    conditions,
    choices,
    default="Medium Risk"
)
df.to_csv(
    "data/cleaned_loan_data.csv",
    index=False
)

df.to_sql(
    "loan_risk_data",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Data Loaded Successfully")

print(df.head())

print(df.info())

print(df[['age_group',
          'income_category',
          'credit_category',
          'risk_category']].head())


df["credit_score"] = (
    df["credit_score"]
    .astype(str)
    .str.replace("%", "", regex=False)
    .astype(float)
)


print(df["credit_score"].describe())

print(df["credit_score"].head(10))
print(df["credit_category"].value_counts(dropna=False))


print("done")