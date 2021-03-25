#!/usr/bin/python3
"""Print state of database that has the letter a
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import MySQLdb
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    sm = sessionmaker(bind=engine)
    session = sm()

    item = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)
    for state in item:
        print("{}: {}".format(state.id, state.name))
    session.close()
