#!/usr/bin/python3
"""Module for connecting to databse and selecting table"""


from sys import argv
from MySQLdb import connect


if __name__ == "__main__":

    db = connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
