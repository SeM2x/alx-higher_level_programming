#!/usr/bin/python3
"""defines a State class"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import declarative_base, relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, autoincrement='auto')
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", backref="states")
