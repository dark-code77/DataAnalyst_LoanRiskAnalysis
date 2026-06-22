from sqlalchemy import create_engine

username = "your username"
password = "your password"
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