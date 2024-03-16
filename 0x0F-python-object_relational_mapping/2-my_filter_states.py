#!/usr/bin/python3
"""takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if (__name__ == '__main__'):
    argv = sys.argv
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]
    ARG = argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=USER, passwd=PASS, db=DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' \
        ORDER BY id ASC".format(ARG))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
