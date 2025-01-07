# book/utils/db_operations.py
from sqlalchemy import create_engine

# Replace with your PostgreSQL database connection details
DATABASE_URL = "postgresql://username:password@localhost:5432/yourdatabase"

# Create engine
engine = create_engine(DATABASE_URL)

# Function to fetch data from a table
def fetch_data():
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM your_table_name")
        return result.fetchall()
