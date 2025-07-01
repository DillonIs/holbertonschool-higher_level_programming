#!/usr/bin/python3
"""Filter based on 2-my_filter_states but prevent
SQL injections"""
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

    # Sanitize by using %s (for script) in place of each variable
    cursor.execute("""
                   SELECT * FROM states
                   WHERE name = BINARY %s
                   ORDER BY id ASC
                   """, (state_name,))

    result = cursor.fetchall()

    for state in result:
        print(state)

    cursor.close()
    db.close()
