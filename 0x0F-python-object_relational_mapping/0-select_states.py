#!/usr/bin/python3
import MySQLdb
import sys

argv = sys.argv
HOST = 'localhost'
PORT = 3306
USER = argv[1]
PASS = argv[2]
DB = argv[3]

if (__name__ == '__main__'):
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
