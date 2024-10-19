import mysql.connector
from mysql.connector import Error

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",   # MySQL host (localhost)
        user="root",        # MySQL username
        password="",        # MySQL password (empty here)
        database="sql"      # Database name
    )
    return connection

# Function to update registration details by ID
def update_registration(id, name=None, email=None, dob=None, phone_number=None):
    conn = None
    try:
        conn = get_db_connection()  # Get database connection
        cursor = conn.cursor()

        # Create a list to hold the updates and the corresponding values
        updates = []
        values = []

        # Add updates based on the provided parameters
        if name:
            updates.append("Name = %s")
            values.append(name)
        if email:
            updates.append("Email = %s")
            values.append(email)
        if dob:
            updates.append("DateOfBirth = %s")
            values.append(dob)
        if phone_number:
            updates.append("PhoneNumber = %s")
            values.append(phone_number)

        # Ensure that at least one field is provided to update
        if not updates:
            print("No fields to update.")
            return

        # Join the updates to form the SET part of the SQL statement
        updates_str = ", ".join(updates)

        # SQL Query to update the record
        query = f"UPDATE Registration SET {updates_str} WHERE ID = %s"
        values.append(id)  # Append the ID to the values list

        cursor.execute(query, values)  # Execute the query with values
        conn.commit()  # Commit the changes to the database
        
        if cursor.rowcount > 0:
            print(f"Registration with ID {id} updated successfully.")
        else:
            print(f"No record found with ID {id}.")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()  # Close cursor
            conn.close()    # Close connection
            print("MySQL connection is closed.")

# Example Usage: Update a registration
update_registration(id=1, name='Sai Updated', email='updated_email@gmail.com', phone_number='9876543210')
