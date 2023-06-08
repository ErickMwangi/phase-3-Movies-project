#!/usr/bin/env python3
import random
from models import User, Movie, Genre, user_movies
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import ipdb;
from faker import  Faker

if __name__ == "__main__":
    engine = create_engine("sqlite:///movies.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    fake=Faker()
ipdb.set_trace()