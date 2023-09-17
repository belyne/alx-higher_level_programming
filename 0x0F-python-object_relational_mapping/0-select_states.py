#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
This script connects to a MySQL server and retrieves a list of states
from the database hbtn_0e_0_usa. It then prints the results to the console.

Usage:
    ./0-select_states.py <username> <password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
