#!/usr/bin/python3
"""Print all city objects
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City
import MySQLdb
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    sm = sessionmaker(bind=engine)
    session = sm()

    item = session.query(
        City,
        State).filter(
        City.state_id == State.id).order_by(
        City.id).all(
    )
    for c, s in item:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
