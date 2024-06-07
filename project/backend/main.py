"""This file  has theentry point implementtion for RESTapi services."""

from typing import List
import uvicorn
from fastapi import Body, FastAPI, HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from film import Film, FilmDB
from review import Review
from user import User, UserDB, LoginModel

app = FastAPI()

engine_users = create_engine("postgresql://postgres:Bullrock@localhost:5432/project-users")
engine_films = create_engine("postgresql://postgres:Bullrock@localhost:5432/films")

@app.post("/users/register")
def register_user(user: User = Body(...)):
    """This method registers a new user"""

    session_maker = sessionmaker(bind=engine_users)
    session = session_maker()

    existing_user = session.query(UserDB).filter_by(username=user.username).first()
    if existing_user is not None:
        return {"message": "Username is already in use. Please choose another one."}

    new_user = UserDB(
        username=user.username,
        password=user.password,
        email=user.email,
    )
    session.add(new_user)
    session.commit()
    session.close()
    return {"message": "User registered successfully"}


@app.post("/users/login")
def login(user: LoginModel):
    """This method logs in a user"""
    dbusername = user.username
    dbpassword = user.password

    session_maker = sessionmaker(bind=engine_users)
    session = session_maker()
    user_db = session.query(UserDB).filter_by(username=dbusername).first()
    session.close()

    if user_db is not None and user_db.password == dbpassword:
        return {"message": "User logged in successfully"}

    raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/films", response_model=List[Film])
def search_films(title: str):
    """This method search a film by the title"""

    if not title.strip():
        raise HTTPException(
            status_code=400, detail="Title must not be empty or only whitespace"
        )

    session_maker = sessionmaker(bind=engine_films)
    session = session_maker()
    films = session.query(Film).filter(Film.title.contains(title)).all()
    session.close()

    return films


@app.get("/films/{film_id}", response_model=Film)
def get_film_details(film_id: int):
    """This method returns all the details of a film"""

    session_maker = sessionmaker(bind=engine_films)
    session = session_maker()
    film = session.query(Film).filter(Film.id == film_id).first()
    session.close()

    if film is None:
        raise HTTPException(status_code=404, detail=f"Film with id {film_id} not found")

    return film


@app.post("/films/{film_id}/review")
def add_film_review(film_id: int, review: Review = Body(...)):
    """This method adds a review to a film"""

    session_maker = sessionmaker(bind=engine_films)
    session = session_maker()
    film = session.query(Film).filter(Film.id == film_id).first()

    if film is None:
        session.close()
        raise HTTPException(status_code=404, detail=f"Film with id {film_id} not found")

    new_review = Review(
        username=review.username,
        text=review.text,
        likes=None,
        replies=None,
    )

    film.reviews.append(new_review)
    session.commit()
    session.close()

    return {"message": "Review added successfully"}


@app.get("/films/{film_id}/reviews", response_model=List[Review])
def get_film_reviews(film_id: int):
    """This method returns all the reviews of a film"""

    session_maker = sessionmaker(bind=engine_films)
    session = session_maker()
    film = session.query(Film).filter(Film.id == film_id).first()
    session.close()

    if film is None:
        raise HTTPException(status_code=404, detail=f"Film with id {film_id} not found")

    return film.reviews


@app.post("/users/{user_id}/watchlist")
def add_film_to_watchlist(user_id: int, film_id: int = Body(...)):
    """This method adds a film to a user's watchlist"""

    session_maker = sessionmaker(bind=engine_users)
    session = session_maker()
    user = session.query(User).filter(User.username == user_id).first()

    if user is None:
        session.close()
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    film = session.query(Film).filter(Film.id == film_id).first()

    if film is None:
        session.close()
        raise HTTPException(status_code=404, detail=f"Film with id {film_id} not found")

    user.watchlist.append(film)
    session.commit()
    session.close()

    return {"message": "Film added to watchlist successfully"}


@app.post("/admin/films")
def add_film_to_catalog(film: Film = Body(...)):
    """This method adds a film to the catalog"""

    new_film = FilmDB(
        title=film.title,
        code=film.code,
        director=film.director,
        year=film.year,
        synopsis=film.synopsis,
        ratings=None,
        reviews=None,
        lenght=film.lenght,
        crew=film.crew,
    )

    session_maker = sessionmaker(bind=engine_films)
    session = session_maker()

    session.add(new_film)
    session.commit()

    return {"message": "Film added to catalog successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

