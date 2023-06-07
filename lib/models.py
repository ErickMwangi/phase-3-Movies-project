#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///movies.db")

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer(), primary_key=True)
    title = Column(String(), index=True)
    release_year = Column(Integer(), index=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String)
    age = Column(Integer, index=True)

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)

class WatchedMovie(Base):
    __tablename__ = "watched_movies"
    user_id = Column(Integer(), ForeignKey("users_id"))
    movie_id = Column(Integer(),ForeignKey("movie_id"))