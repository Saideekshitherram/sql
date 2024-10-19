import mysql.connector
from mysql.connector import Error

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",   # MySQL host (
        user="root",        # MySQL username
        password="",        # MySQL password 
        database="sql"      # Database name
    )
    return connection

# Function to insert a registration record into the table
def create_registration(name, email, dob, phone_number):
    conn = None
    try:
        conn = get_db_connection()  # Get database connection
        cursor = conn.cursor()

        # SQL Query 
        query = """
        INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber)
        VALUES (%s, %s, %s, %s)
        """
        
        # Values to insert into the table
        values = (name, email, dob, phone_number)
        
        cursor.execute(query, values)  # Execute the query with values
        conn.commit()  # Commit the changes to the database
        
        print(f"Registration added successfully for {name}.")
    
    except Error as e:
        print(f"Error: {e}")  # Print any error that occurs during execution
    
    finally:
        if conn and conn.is_connected():
            cursor.close()  # Close cursor
            conn.close()    # Close connection
            print("MySQL connection is closed.")

# Test the function
create_registration('Sai', 'erram.sai@gmail.com', '2002-09-25', '1234567890')
