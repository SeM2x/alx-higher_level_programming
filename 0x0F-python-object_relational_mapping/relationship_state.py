#!/usr/bin/python3
"""
defines a State class
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    State class
    """
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, autoincrement='auto')
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", back_populates="state")
