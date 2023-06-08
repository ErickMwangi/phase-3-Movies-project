from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert

from models import Movie, User, Genre, user_movies

if __name__ == "__main__":
    engine = create_engine("sqlite:///movies.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Movie).delete()
    session.query(Genre).delete()
    session.query(User).delete()
    session.query(user_movies).delete()
    fake = Faker()

    users = []
    for _ in range(20):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(user)
        users.append(user)

    movies = []
    for _ in range(20):
        movie = Movie(
            name=fake.unique.name(),
            price=random.randint(200,500)
        )
        session.add(movie)
        movies.append(movie)

    existing_combinations = set()
    for _ in range(50):
        user_id = random.randint(1, 20)
        movie_id = random.randint(1, 20)

        if (user_id, movie_id) in existing_combinations:
            continue
        existing_combinations.add((user_id, movie_id))
        user_movie_data = {"user_id": user_id, "movie_id": movie_id}
        stmt = insert(user_movies).values(user_movie_data)
        session.execute(stmt)

    for _ in range(50):
        genre = Genre(
            star_rating=random.randint(1, 5),
            user_id=random.randint(1, 20),
            movie_id= random.randint(1, 20)
        )
        session.add(genre)

    session.commit()
    session.close()    
    


