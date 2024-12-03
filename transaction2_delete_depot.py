from db_connection import get_connection

def delete_depot(depid):
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Step 1: Check if the depot exists in the Depot table
        cursor.execute("SELECT depid FROM Depot WHERE depid = %s;", (depid,))
        depot_exists = cursor.fetchone()

        if depot_exists is None:
            print(f"Depot {depid} does not exist anymore.")
            return  # Exit the function if the depot is not found

        # Step 2: Delete the depot from Stock first to maintain referential integrity
        cursor.execute("DELETE FROM Stock WHERE depid = %s;", (depid,))

        # Step 3: Now, delete the depot from Depot table
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
