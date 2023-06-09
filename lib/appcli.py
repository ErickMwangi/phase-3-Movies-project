import click
from sqlalchemy.orm import sessionmaker
from models import User, Movie, Genre
from sqlalchemy import  (create_engine)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///movies.db")
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def create_db():
    engine = create_engine("sqlite:///movies.db")
    Base.metadata.create_all(engine)
    print("database created successfully")

@cli.command()
@click.option("--price", prompt="enter price")
@click.option("--name", prompt="enter movie name")
def add_movie(price, name):
    movie = Movie(price=price, name=name)
    session.add(movie)
    session.commit()
    print("movie added successfully")

@cli.command()
@click.option("--first-name", prompt="enter first name")
@click.option("--last-name", prompt="enter last name")
def add_user(first_name, last_name):
    user = User(first_name=first_name, last_name=last_name)
    session.add(user)
    session.commit()
    print("user added successfully")

@cli.command()
@click.option("--star-rating", prompt="enter star rating")
@click.option("--user-id", prompt="enter user id")
@click.option("--movie-id", prompt="enter movie id")
def add_genre(star_rating, user_id, movie_id):
    genre = Genre(star_rating=star_rating, user_id=user_id, movie_id=movie_id)
    session.add(genre)
    session.commit()
    print("genre added successfully")


if __name__ == "__main__":
    cli()


    
