#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  

if __name__ == "__main__":  
    engine = create_engine("sqlite:///movies.db")
    Session = sessionmaker(bind=engine)
    session = Session()

user_movies = Table(
    "user_movies",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    extend_existing=True,
)    
class User(Base):
     __tablename__ = "users"
 
     id = Column(Integer(), primary_key=True)
     first_name = Column(String())
     last_name = Column(String())
     genres = relationship("Genre", backref=backref ("user"))
     movies = relationship("Movie", secondary="user_movies", back_populates="users")
 
     def __repr__(self):
         return f'User: {self.first_name} {self.last_name}'
     def user_genr(self):
         return self.genres
     def user_mov(self):
         return self.movies
     def full_name(self):
         return f'{self.first_name} {self.last_name}'
     def favorite_movie(self):
         favorite_movie = session.query(Movie).order_by(Movie.star_rating.desc()).first()
         return favorite_movie
     def add_genre(self, movie, rating, session):
         genre = Genre(user=self, movie=movie, star_rating=rating)
         session.add(genre)
         session.commit()
     def delete_genres(self, movie, session):
         genres_to_delete = [genre for genre in self.genres if genre.movie == movie]
         for genre in genres_to_delete:
             session.delete(genre)
             session.commit()
         
 
 
class Movie(Base):
     __tablename__ = "movies"
     id = Column(Integer(), primary_key=True)
     name = Column(String())
     price = Column(Integer())
     genres = relationship("Genre", backref=backref ("movie"))
     users = relationship("User", secondary="user_movies", back_populates="movies" )
 
     def __repr__(self):
         return f"name={self.name}, price={self.price})"
     
     @classmethod
     def get_movies(cls,session):
         movies = session.query(cls).all()
         movie_data = []
         for movie in movies:
             movie_data.append({"name": movie.name})
         return movie_data
 
     @classmethod
     def add_movie(cls, session, name):
         movie = cls(name=name)
         session.add(movie)
         session.commit()
         return "Movie added successfully"
     
     @classmethod
     def update_movie(cls, session, movie_id, new_name):
         movie = session.query(cls).get(movie_id)
         if movie:
             movie.name = new_name
             session.commit()
             return "Movie updated successfully!"
         else:
             return "Movie not found!"
         
     @classmethod
     def delete_movie(cls, movie_id, session):
         movie = session.query(cls).get(movie_id)
         if movie:
             session.delete(movie)
             session.commit()
             return "Movie deleted successfully!"
         else:
             return "Movie not found!"
 
 
class Genre(Base):
     __tablename__ = "genres"
     id = Column(Integer(), primary_key=True)
     star_rating = Column(Integer())
     user_id = Column(Integer(), ForeignKey("users.id"))
     movie_id = Column(Integer(), ForeignKey("movies.id"))
 
     def user(self):
         return self.user
     def movie(self):
         return self.movie
     def full_genre(self):
         return f"Review for {self.movie.name()} by {self.user.full_name()}: {self.star_rating} stars."
     def __repr__(self):
         return f'Genre(id={self.id}, ' + \
             f'star_rating={self.star_rating}, ' + \
             f'movie_id={self.movie_id}), ' +\
             f'user_id={self.user_id})'
     
 