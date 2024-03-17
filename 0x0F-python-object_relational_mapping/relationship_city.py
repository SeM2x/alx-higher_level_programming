#!/usr/bin/python3
"""defines a City class"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column('id', Integer, primary_key=True, autoincrement='auto')
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey(
        'states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
