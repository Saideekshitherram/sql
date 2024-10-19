import mysql.connector
from mysql.connector import Error

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",   # MySQL host 
        user="root",        # MySQL username
        password="",        # MySQL password 
        database="sql"      # Database name
    )
    return connection

# Function to read all registrations from the table
def read_registrations():
    conn = None
    try:
        conn = get_db_connection()  # Get database connection
        cursor = conn.cursor()

        # SQL Query 
        query = "SELECT * FROM Registration"
        cursor.execute(query)

        # Fetch all rows from the result
        records = cursor.fetchall()

        # Print the result in a readable format
        print("Registrations:")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Date of Birth: {row[3]}, Phone: {row[4]}, Registration Date: {row[5]}")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()  # Close cursor
            conn.close()    # Close connection
            print("MySQL connection is closed.")

# Call the function to read all registrations
read_registrations()
