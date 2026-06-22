from sqlalchemy import create_engine

username = "postgres"
password = "Abhi123"
host = "localhost"
port = "5432"
database = "loan_analysis"

try:
    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    )
    conn = engine.connect()

    print("Database Connected Successfully")

    conn.close()

except Exception as e:
    print("Error:", e)