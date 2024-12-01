from db_connection import get_connection

def add_depot_and_stock(depid, address, volume, prodid, quantity):
    conn = get_connection()
    if conn is None:
        return

    try:
        conn.autocommit = False  # Start transaction
        cursor = conn.cursor()

        # Add the new depot to the Depot table
        cursor.execute("INSERT INTO Depot (depid, addr, volume) VALUES (%s, %s, %s);", (depid, address, volume))

        # Add the stock for the existing product in the new depot
        cursor.execute("INSERT INTO Stock (prodid, depid, quantity) VALUES (%s, %s, %s);", (prodid, depid, quantity))

        # Commit the transaction
        conn.commit()
        print(f"Depot {depid} added successfully with stock for product {prodid}.")
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print("Error during transaction:", e)
    finally:
        cursor.close()
        conn.close()

# Test the function
add_depot_and_stock('d100', 'Chicago', 100, 'p1', 100)  # Add a new depot and stock
