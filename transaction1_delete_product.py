from db_connection import get_connection

def delete_product(prodid):
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Delete the product from Stock first to maintain referential integrity
        cursor.execute("DELETE FROM Stock WHERE prodid = %s;", (prodid,))

        # Now, delete the product from Product table
        cursor.execute("DELETE FROM Product WHERE prodid = %s;", (prodid,))

        # Commit the transaction
        conn.commit()
        print(f"Product {prodid} deleted successfully.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

# Test the function
delete_product('p1')  # Delete product p1
