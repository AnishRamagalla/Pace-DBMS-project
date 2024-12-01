**CS623 Project - Database Transactions with PostgreSQL and Python**
This project focuses on tasks like adding, renaming, and deleting products and depots from the Stock table, ensuring data consistency and reliability. It demonstrates practical database transactions that adhere to ACID properties.

**Features**
1. Add Products and Stock: Add new products to the Product table and their corresponding stock to the Stock table.
2. Rename Products and Depots: Rename products and depots, ensuring consistency between related tables using ON UPDATE CASCADE foreign key relationships.
3. Delete Products and Depots: Safely delete products and depots, maintaining referential integrity.
4. ACID Compliance: All operations follow the ACID properties to ensure data integrity.

**Technologies Used**
1. PostgreSQL: For database management.
2. Python: For implementing the database operations and transactions
3. psycopg2: A PostgreSQL adapter for Python.
4. Git: For version control and collaboration.

**Prerequisites**
To run this project, make sure to have the following installed on your system:
1. PostgreSQL: Make sure PostgreSQL is installed and running.
2. Python: Python 3.x (preferably 3.6 or higher) is required.
3. psycopg2: The PostgreSQL adapter for Python:
   pip3 install psycopg2-binary

**Setting Up the Database**
1. Create the Database:
   CREATE DATABASE cs623_project;

2. Create tables such as Product, Depot and Stock.

   Product:
   
   CREATE TABLE Product (prodid CHAR(10), pname  VARCHAR(30), price DECIMAL);
   
   ALTER TABLE Product ADD CONSTRAINT pk_product PRIMARY KEY (prodid);
   
   ALTER TABLE Product ADD CONSTRAINT ck_product_price CHECK (price > 0);
   
   INSERT INTO Product (prodid, pname, price) VALUES ('p1', 'tape', 2.5), ('p2', 'tv', 250), ('p3', 'vcr', 80);
   
   Depot:
   
   CREATE TABLE Depot ( depid CHAR(10), addr VARCHAR(50), volume INT );
   
   ALTER TABLE Depot ADD CONSTRAINT pk_depot PRIMARY KEY (depid);
   
   INSERT INTO Depot (depid, addr, volume) VALUES ('d1', 'New York', 9000), ('d2', 'Syracuse', 6000), ('d4','New York', 2000);
   
   Stock:
   
   CREATE TABLE Stock ( prodid CHAR(10), depid CHAR(10), quantity INT );
   
   ALTER TABLE Stock ADD CONSTRAINT pk_stock PRIMARY KEY (prodid, depid);
   
   ALTER TABLE Stock ADD CONSTRAINT fk_stock_product FOREIGN KEY (prodid) REFERENCES Product(prodid);
   
   ALTER TABLE Stock ADD CONSTRAINT fk_stock_depot FOREIGN KEY (depid) REFERENCES Depot(depid);
   
   INSERT INTO Stock (prodid, depid, quantity) VALUES ('p1', 'd1', 1000), ('p1', 'd2', -100), ('p1', 'd4', 1200), ('p3', 'd1', 3000), ('p3', 'd4', 2000), ('p2', 'd4', 1500), ('p2', 'd1', -400), ('p2', 'd2', 2000);

**How to use:**
1. Clone the Repository:
   git clone https://github.com/UserName/cs623_project.git
   
3. Configure Database Connection: In your Python scripts (e.g., db_connection.py), ensure the PostgreSQL connection credentials are correct:
   conn = psycopg2.connect(
   dbname="database name",  # database name
   user="username",         # PostgreSQL username
   password="your_password",  # PostgreSQL password
   host="localhost",        # Database host
   port="5432"              # Database port
)
4. Run the Python Scripts: After setting up the database, run the provided Python scripts to perform the transactions. Transactions that are performed in this project are:
a. We add a product (p100, cd, 5) in Product and (p100, d2, 50) in Stock.
b. We add a depot (d100, Chicago, 100) in Depot and (p1, d100, 100) in
Stock.
c. The product p1 changes its name to pp1 in Product and Stock.
d. The depot d1 changes its name to dd1 in Depot and Stock
e. The product p1 is deleted from Product and Stock.
f. The depot d1 is deleted from Depot and Stock.

**Contact:**

If you have any questions or feedback, feel free to contact me at:

Email: nisargavgowda15@gmail.com

GitHub: Nisarga15
