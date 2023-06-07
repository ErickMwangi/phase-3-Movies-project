#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if __name__ == "__main__":
   
   engine = create_engine("sqlite:///movies.db")
   Session = sessionmaker(bind=engine)
   session = Session()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer(), primary_key=True)
    title = Column(String(), index=True)
    release_year = Column(Integer(), index=True)
    genre_id = Column(Integer, ForeignKey("genres.id"))

    def __repr__(self):
        return f"Movie(id={self.id}, title={self.title}, release_year={self.release_year}, genre_id={self.genre_id})"
    
    @classmethod
    def get_movies(cls,session):
        movies = session.query(cls).all()
        for movie in movies:
            print(movie.title, movie.release_year)

    @classmethod
    def add_movie(cls, session, title, release_year):
        movie = cls(title=title, release_year=release_year)
        session.add(movie)
        session.commit()
        return "Movie added successfully"
    
    @classmethod
    def update_movie(cls, session, movie_id, new_title):
        movie = session.query(cls).get(movie_id)
        if movie:
            movie.title = new_title
            session.commit()
            return "Movie updated successfully!"
        else:
            return "Movie not found!"
        
    @classmethod
    def delete_movie(cls, session, movie_id):
        movie = session.query(cls).get(movie_id)
        if movie:
            session.delete(movie)
            session.commit()
            return "Movie deleted successfully!"
        else:
            return "Movie not found!"

        
            

    


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String)
    age = Column(Integer, index=True)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, age={self.age})"
        

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)


# class WatchedMovie(Base):
#     __tablename__ = "watched_movies"
#     user_id = Column(Integer(), ForeignKey("users_id"))
#     movie_id = Column(Integer(),ForeignKey("movie_id"))