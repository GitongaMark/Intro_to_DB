import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username if different
            password='@M.29g.11k.03'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
