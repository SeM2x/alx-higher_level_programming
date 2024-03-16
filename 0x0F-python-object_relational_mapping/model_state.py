#!/usr/bin/python3
"""defines a State class"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, autoincrement='auto')
    name = Column('name', String, nullable=False)
