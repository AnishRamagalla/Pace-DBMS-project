from db_connection import get_connection

def add_product_and_stock(prodid, pname, price, depid, quantity):
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Add the new product to the Product table
        cursor.execute("INSERT INTO Product (prodid, pname, price) VALUES (%s, %s, %s);", (prodid, pname, price))

        # Add the new stock to the Stock table
        cursor.execute("INSERT INTO Stock (prodid, depid, quantity) VALUES (%s, %s, %s);", (prodid, depid, quantity))

        # Commit the transaction
        conn.commit()
        print(f"Product {prodid} added successfully with stock in depot {depid}.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

# Test the function
add_product_and_stock('p100', 'cd', 5, 'd2', 50)  # Add a new product and stock
