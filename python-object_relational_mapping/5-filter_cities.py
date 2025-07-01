#!/usr/bin/python3
"""Filter cities by state and prevent SQL injections"""
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

    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = BINARY %s
        ORDER BY cities.id ASC
        """, (state_name,)
        )
    result = cursor.fetchall()

    cities = []
    for state in result:
        cities.append(state[0])
    print(", ".join(cities))

    cursor.close()
    db.close()
