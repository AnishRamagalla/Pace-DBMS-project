from db_connection import get_connection

def add_cascade_to_foreign_key():
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Step 1: Drop the existing foreign key constraint
        cursor.execute("""
            ALTER TABLE Stock DROP CONSTRAINT fk_stock_product;
        """)

        # Step 2: Add the foreign key constraint with ON UPDATE CASCADE
        cursor.execute("""
            ALTER TABLE Stock
            ADD CONSTRAINT fk_stock_product
            FOREIGN KEY (prodid) REFERENCES Product (prodid) ON DELETE CASCADE ON UPDATE CASCADE;
        """)

        # Commit the transaction
        conn.commit()
        print("Foreign key constraint updated with ON UPDATE CASCADE.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

def rename_product(old_prodid, new_prodid):
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Step 1: Update the product ID in the Product table
        cursor.execute("UPDATE Product SET prodid = %s WHERE prodid = %s;", (new_prodid, old_prodid))

        # Step 2: Commit the transaction
        conn.commit()
        print(f"Product {old_prodid} renamed to {new_prodid}.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

# Step 3: Execute both tasks
def main():
    # Add the ON UPDATE CASCADE to the foreign key constraint
    add_cascade_to_foreign_key()

    # Now that the foreign key is updated, rename the product
    rename_product('p1', 'pp1')  # Rename product p1 to pp1

# Run the main function
if __name__ == "__main__":
    main()
