#!/usr/bin/python3
"""
    model_state.py
    Set up for Class State, learning SQLAlchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
        State class inherits from Base
    """

    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
        )

    name = Column(
        String(128),
        nullable=False
        )
