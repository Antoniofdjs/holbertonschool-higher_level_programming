#!/usr/bin/python3
"""
    model_state.py
    Set up for Class City, learning SQLAlchemy
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
        Class for table cities, inherits from Base
    """
    __tablename__ = 'cities'

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

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
        )
