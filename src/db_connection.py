from sqlalchemy import create_engine

# Replace these values with your actual database credentials
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'your_database'

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Example: Test the connection
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT version();")
            print(result.fetchone())
    except Exception as e:
        print(f"Database connection failed: {e}")
        def load_data_to_db(query, params=None):
            """
            Executes an INSERT/UPDATE/DELETE query with optional parameters.
            """
            try:
                with engine.begin() as connection:
                    connection.execute(query, params or {})
                print("Data loaded successfully.")
            except Exception as e:
                print(f"Failed to load data: {e}")