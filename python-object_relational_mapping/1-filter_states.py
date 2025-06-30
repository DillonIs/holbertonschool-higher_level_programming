#!/usr/bin/python3
"""Python script to filter database output"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )
    # Create a cursor and execute a SQL query
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id')

    result = cursor.fetchall()
    for state in result:
        if state[1][0] == "N":
            print(state)

    # Close when complete
    cursor.close()
    db.close()
