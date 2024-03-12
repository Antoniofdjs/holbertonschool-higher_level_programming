#!/usr/bin/python3
"""
    model_state.py
    Set up for Class State, learning SQLAlchemy
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':

    # Collect data from argv arguments
    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    # Make connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}'
        )

    # Make 'cursor'
    session = sessionmaker(bind=engine)
    session = session()

    # Fetch only first row
    states = session.query(State).filter(State.name.like('%a%'))

    if states:
        for state in states:
            print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
