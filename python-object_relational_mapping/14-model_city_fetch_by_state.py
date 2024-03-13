#!/usr/bin/python3
"""
    model_state.py
    Delete
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

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

    # Inner join for cities and states tables
    rows = session.query(City, State)\
        .join(State, City.state_id == State.id)\
        .order_by(City.id)\
        .all()

    for city, state in rows:  # Unpacking [(city_object, state_object)...]
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
