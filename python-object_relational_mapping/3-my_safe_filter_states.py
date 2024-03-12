#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

"""


from sys import argv
from MySQLdb import connect

if __name__ == '__main__':

    db = connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE %s\
        ORDER BY name ASC"  # Prevent sql injection
    cursor.execute(query, (argv[4],))  # Prevent sql injection

    rows = cursor.fetchall()  # Retrives all selected items, in tuple ((), ())

    for row in rows:
        print("{}".format(row))

    cursor.close()
    db.close()
