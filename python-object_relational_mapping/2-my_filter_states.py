#!/usr/bin/python3
"""Filter based on argv [4] user input"""
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
    state_name = sys.argv[4]
    # Create a cursor and execute a SQL query
    cursor = db.cursor()

    cursor.execute("""
                   SELECT * FROM states
                   WHERE name = BINARY '{}'
                   ORDER BY id asc
                   """.format(state_name))

    result = cursor.fetchall()

    for state in result:
        print(state)

    cursor.close()
    db.close()
