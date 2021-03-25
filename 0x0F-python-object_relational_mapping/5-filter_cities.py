#!/usr/bin/python3
"""
List cities of state passed as argument, injection free
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities JOIN states \
	ON cities.state_id = states.id WHERE states.name LIKE %s \
	ORDER BY cities.id", (argv[4],))
    output = cur.fetchall()

    for item in output:
        print(", ".join(item[0] for item in output))
    cur.close()
    db.close()
