#!/usr/bin/python3
"""lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa"""
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
    cur.execute("SELECT * FROM states WHERE name \
            LIKE BINARY 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
