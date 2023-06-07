#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///movies.db")

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer(), primary_key=True)
    title = Column(String(), index=True)
    release_year = Column(Integer(), index=True)

    