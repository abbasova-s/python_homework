# Task 1: Create a New SQLite Database
import sqlite3

# Connect to a new SQLite database
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()
        print("Database created and connected successfully.")

        conn.execute("PRAGMA foreign_keys = 1")


# Task 2: Define Database Structure
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers(
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines(
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers(
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions(
        subscriptions_id INTEGER PRIMARY KEY,
        expiration_date TEXT NOT NULL,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
        UNIQUE (subscriber_id, magazine_id)
        )
        """)        

except sqlite3.Error as e:
    print(f"Database error: {e}")


# Task 3: Populate Tables with Data
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()

        def add_publisher(cursor, name):
            try:
                cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
            except sqlite3.IntegrityError:
                print(f"Publisher {name} is already in database.")

        def add_magazine(cursor, name, publisher_id):
            try:
                cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",(name, publisher_id))
            except sqlite3.IntegrityError:
                print(f"Magazine {name} is already in database.")

        def add_subscriber(cursor, name, address):
            try:
                cursor.execute("""SELECT subscriber_id FROM subscribers
                WHERE name = ? AND address = ? """, (name, address))
                existing_subscriber = cursor.fetchone()
                if existing_subscriber is None:
                    cursor.execute(""" INSERT INTO subscribers (name, address) VALUES (?,?)""", (name, address))
                else:
                    print(f"Subscriber {name} is already in database.")
            except sqlite3.Error as e:
                print(f"Error adding subscriber: {e}")

        def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
            try:
                cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))
            except sqlite3.IntegrityError:
                print(f"Subscription is already in database.")


        # Add publishers
        add_publisher(cursor, "Hachette Livre")
        add_publisher(cursor, "Conde Nast")
        add_publisher(cursor, "Fortune Media IP Limited")

        # Add magazines
        add_magazine(cursor, "ELLE", 1)
        add_magazine(cursor, "Vogue", 2)
        add_magazine(cursor, "Fortune", 3)

        # Add subscribers
        add_subscriber(cursor, "Timur Toktiev", "12 Park St")
        add_subscriber(cursor, "Kamila Ashurova", "234 Beach St")
        add_subscriber(cursor, "Alex Toktiev", "99 Broadway Ave")

        # Add subscriptions
        add_subscription(cursor, 1, 1, "2025-01-01")
        add_subscription(cursor, 2, 2, "2026-06-15")
        add_subscription(cursor, 3, 3, "2027-01-31")

        conn.commit()
        print("Sample data inserted")


        # Task 4: Write SQL Queries
        # Query to retrieve all information from the subscribers table:
        cursor.execute("SELECT * FROM subscribers")
        result = cursor.fetchall()
        for row in result:
            print(row)

        # Query to retrieve all magazines sorted by name:
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        result = cursor.fetchall()
        for row in result:
            print(row)

        # Query to find magazines for a particular publisher:
        cursor.execute("""SELECT * FROM magazines JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?""", ("Hachette Livre",))
        result = cursor.fetchall()
        for row in result:
            print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")





