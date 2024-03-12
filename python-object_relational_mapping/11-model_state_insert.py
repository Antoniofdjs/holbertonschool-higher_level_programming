#!/usr/bin/python3
"""
    model_state.py
    Create a new state and add to table
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
    state_name = argv[4]

    # Make connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}'
        )

    # Make 'cursor'
    session = sessionmaker(bind=engine)
    session = session()

    new_state = State(name=state_name)

    session.add(new_state)
    session.commit()  # Commit the transaction

    session.close()
