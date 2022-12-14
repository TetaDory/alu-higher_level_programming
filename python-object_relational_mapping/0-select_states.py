#!/usr/bin/python3
"""Creating a script that lists all states from a database"""

import sys
import MySQLdb


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],)

    cur = db_conn.cursor()

    cur.execute(
        "SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db_conn.close()
