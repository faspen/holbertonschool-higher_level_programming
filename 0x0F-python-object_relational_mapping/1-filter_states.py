#!/usr/bin/python3
"""
List states starting with 'N'
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    output = cursor.fetchall()

    for item in output:
        print(item)
    cursor.close()
    db.close()
