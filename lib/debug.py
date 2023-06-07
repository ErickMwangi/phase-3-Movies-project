#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import ipdb;

if __name__ == "__main__":
    engine = create_engine("sqlite:///movies.db")
    Session = sessionmaker(bind=engine)
    session = Session()

ipdb.set_trace()