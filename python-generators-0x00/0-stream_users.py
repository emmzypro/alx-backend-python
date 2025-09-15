#!/usr/bin/python3
import mysql.connector

def stream_users():
    """Generator function that streams rows from user_data table one by one."""
    try:
        # 1. Connect to ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # <-- change if using another MySQL user
            password="your_password",  # <-- change to your MySQL password
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)  # dictionary=True returns rows as dicts
        cursor.execute("SELECT * FROM user_data")

        # 2. Single loop yielding one row at a time
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

