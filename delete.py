import mysql.connector
from mysql.connector import Error

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",   # MySQL host 
        user="root",        # MySQL username
        password="",        # MySQL password (empty here)
        database="sql"      # Your database name
    )
    return connection

# Function to delete a registration by ID
def delete_registration_by_id(id):
    conn = None
    try:
        conn = get_db_connection()  # Get database connection
        cursor = conn.cursor()

        # SQL Query to delete the record with a specific ID
        query = "DELETE FROM Registration WHERE ID = %s"
        cursor.execute(query, (id,))

        # Commit the changes to the database
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Registration with ID {id} deleted successfully.")
        else:
            print(f"No record found with ID {id}.")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()  # Close cursor
            conn.close()    # Close connection
            print("MySQL connection is closed.")

# Function to delete a registration by email
def delete_registration_by_email(email):
    conn = None
    try:
        conn = get_db_connection()  # Get database connection
        cursor = conn.cursor()

        # SQL Query to delete the record with a specific email
        query = "DELETE FROM Registration WHERE Email = %s"
        cursor.execute(query, (email,))

        # Commit the changes to the database
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Registration with Email {email} deleted successfully.")
        else:
            print(f"No record found with Email {email}.")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()  # Close cursor
            conn.close()    # Close connection
            print("MySQL connection is closed.")

# Example Usage: Delete a registration by ID
delete_registration_by_id(1)

# Example Usage: Delete a registration by Email
delete_registration_by_email('updated_email@gmail.com')
