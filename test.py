import mysql.connector
from mysql.connector import Error

def test_db_connection():
    try:
        # Database credentials
        connection = mysql.connector.connect(
            host="localhost",        
            user="root",     
            password="", 
            database="sql"  
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
