from db_connection import get_connection

# Function to add ON UPDATE CASCADE to the foreign key constraint
def add_cascade_to_depot_foreign_key():
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Step 1: Drop the existing foreign key constraint
        cursor.execute("""
            ALTER TABLE Stock DROP CONSTRAINT fk_stock_depot;
        """)

        # Step 2: Add the foreign key constraint with ON UPDATE CASCADE
        cursor.execute("""
            ALTER TABLE Stock
            ADD CONSTRAINT fk_stock_depot
            FOREIGN KEY (depid) REFERENCES Depot (depid) ON DELETE CASCADE ON UPDATE CASCADE;
        """)

        # Commit the transaction
        conn.commit()
        print("Foreign key constraint updated with ON UPDATE CASCADE for depot.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

# Function to rename a depot in both Depot and Stock tables
def rename_depot(old_depid, new_depid):
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Step 1: Update the depot ID in the Depot table
        cursor.execute("UPDATE Depot SET depid = %s WHERE depid = %s;", (new_depid, old_depid))

        # Step 2: Commit the transaction
        conn.commit()
        print(f"Depot {old_depid} renamed to {new_depid}.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

# Main function to execute both tasks: updating the foreign key and renaming the depot
def main():
    # Add the ON UPDATE CASCADE to the foreign key constraint
    add_cascade_to_depot_foreign_key()

    # Now that the foreign key is updated, rename the depot
    rename_depot('d1', 'dd1')  # Rename depot d1 to dd1

# Run the main function
if __name__ == "__main__":
    main()
