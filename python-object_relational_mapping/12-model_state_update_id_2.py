#!/usr/bin/python3
"""
    model_state.py
    Update a state
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

    # Update the values and commit
    states = session.query(State).filter(State.id == 2)\
        .update({State.name: "New Mexico"})

    session.commit()

    session.close()
