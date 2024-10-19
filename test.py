import mysql.connector
from mysql.connector import Error

def test_db_connection():
    try:
        # Replace these values with your database credentials
        connection = mysql.connector.connect(
            host="localhost",         # e.g., "localhost"
            user="root",     # e.g., "root"
            password="", # e.g., "password"
            database="sql"  # e.g., "test_db" (optional if connecting to a specific database)
        )
        
        if connection.is_connected():
            print("Connected to the database successfully!")
        
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Test the connection
test_db_connection()
