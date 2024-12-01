from db_connection import get_connection

if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("Connection successful!")
        conn.close()
    else:
        print("Failed to connect to the database.")
