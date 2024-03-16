#!/usr/bin/python3
"""takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if (__name__ == '__main__'):
    argv = sys.argv
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=USER, passwd=PASS, db=DB)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
            FROM cities JOIN states ON cities.state_id=states.id\
            WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC",
                (argv[4],))
    query_rows = cur.fetchall()
    for i, row  in enumerate(query_rows):
        if i != len(query_rows) - 1:
            print(row[0], end=', ')
        else:
            print(row[0])

    cur.close()
    db.close()
