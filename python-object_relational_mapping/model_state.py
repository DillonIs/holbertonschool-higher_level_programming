#!/usr/bin/python3
"""Create a table from Python class State"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Table creation"""
    __statetable__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
