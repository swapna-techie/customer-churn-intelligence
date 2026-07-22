try:
    import psycopg2
except ImportError as exc:
    raise ImportError(
        "psycopg2 is required for database connection. Install it with `pip install psycopg2-binary`."
    ) from exc

connection = psycopg2.connect(
    host="localhost",
    database="customer_churn_db",
    user="postgres",
    password="Swapna reddy18",
    port="1822"
)

print("Database Connected Successfully!")