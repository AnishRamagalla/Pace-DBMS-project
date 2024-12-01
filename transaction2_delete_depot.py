from db_connection import get_connection

def delete_depot(depid):
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Step 1: Delete the depot from Stock first to maintain referential integrity
        cursor.execute("DELETE FROM Stock WHERE depid = %s;", (depid,))

        # Step 2: Now, delete the depot from Depot table
        cursor.execute("DELETE FROM Depot WHERE depid = %s;", (depid,))

        # Commit the transaction
        conn.commit()
        print(f"Depot {depid} deleted successfully.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

# Test the function
delete_depot('d1')  # Delete depot d1
