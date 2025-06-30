#!/usr/bin/python3
"""Python script for selecting states from a MySQL database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL using commandline arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    # Create a cursor and execute a SQL query
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
