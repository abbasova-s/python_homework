import sqlite3

# Task 1: Complex JOINs with Aggregation
# Find the total price of each of the first 5 orders

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT o.order_id, SUM(p.price * li.quantity)
   FROM orders o
   JOIN line_items li
   ON o.order_id = li.order_id
   JOIN products p
   ON p.product_id = li.product_id
   GROUP BY o.order_id
   ORDER BY o.order_id
   LIMIT 5;
"""

cursor.execute(query)

for row in cursor:
    print(row)

conn.close()


# Task 2: Understanding Subqueries
# For each customer, find the average price of their orders


conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT customers.customer_name, AVG(order_totals.total_price) AS average_total_price
FROM customers
LEFT JOIN (
    SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li
    ON o.order_id = li.order_id
    JOIN products p
    ON p.product_id = li.product_id
    GROUP BY o.order_id
) AS order_totals
ON customers.customer_id = order_totals.customer_id_b
GROUP BY customers.customer_id;
"""

cursor.execute(query)

for row in cursor:
    print(row)

conn.close()


# Task 3: An Insert Transaction Based on Data
# new order for the customer named Perez and Sons

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

try:
    # Find customer_id
    customer = conn.execute("""
        SELECT customer_id
        FROM customers
        WHERE customer_name= 'Perez and Sons';
    """).fetchone()

    print("Customer: ", customer)
    customer_id = customer[0]

    # Find 5 cheapest products
    products = conn.execute("""
        SELECT product_id, product_name, price
        FROM products
        ORDER BY price
        LIMIT 5;    
    """).fetchall()
    print("Products: ", products)

    # Find employee_id
    employee = conn.execute("""
        SELECT employee_id
        FROM employees
        WHERE first_name = "Miranda"
        AND last_name = "Harris";    
    """).fetchone()

    print("Employee: ", employee)
    employee_id = employee[0]

    # Create new order
    order = conn.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id;
    """, (customer_id, employee_id)).fetchone()

    order_id = order[0]
    
    # Add line items to the order
    for product_id, product_name, price in products:
        conn.execute("""
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, ?);
        """, (order_id, product_id, 10))

    # Commit
    conn.commit()
    print("Created order:", order_id)

    # Verify the order and line items
    results = conn.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name, p.price
        FROM line_items li
        JOIN products p
            ON li.product_id = p.product_id
        WHERE li.order_id = ?
        ORDER BY li.line_item_id;
    """, (order_id,)).fetchall()

    for row in results:
        print(row)

except Exception as e:
    conn.rollback()
    print("Error: ", e)

conn.close()


# Task 4: Aggregation with HAVING
# Find all employees associated with more than 5 orders

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT (e.first_name || ' ' || e.last_name) AS employee_name, COUNT(o.order_id) AS order_total
FROM employees e
JOIN orders o
ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT (o.order_id) > 5;
"""

cursor.execute(query)

for row in cursor:
    print(row)

conn.close()
