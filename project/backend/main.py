"""This file  has theentry point implementtion for RESTapi services."""

from typing import List

from catalog import Catalog
from fastapi import Body, FastAPI, HTTPException
from film import Film
from review import Review
from user import User

app = FastAPI()


@app.post("/users/register")
def register_user(user: User = Body(...)):
    """This method registers a new user"""

    new_user = User(
        username=user.username,
        password=user.password,
        email=user.email,
        name=user.name,
        rated_films=user.rated_films,
        reviews=user.reviews,
        replies=user.replies,
        fav_films=user.fav_films,
        watchlist=user.watchlist,
    )

    Catalog.users_registered.append(new_user)

    return {"message": "User registered successfully"}

@app.post("/users/login")
def login_user(username: str, password: str):
    """This method logs in a user"""

    user = next((user for user in Catalog.users_registered if user.username == username), None)

    if user is None:
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")

    if user.password != password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {"message": "User logged in successfully"}


@app.get("/films", response_model=List[Film])
def search_films(title: str):
    """This method search a film by the title"""

    if not title.strip():
        raise HTTPException(
            status_code=400, detail="Title must not be empty or only whitespace"
        )

    if Catalog.catalog_films is None:
        raise HTTPException(status_code=500, detail="Film catalog is not available")

    results = [
        film for film in Catalog.catalog_films if title.lower() in film.title.lower()
    ]

    return results


@app.get("/films/{film_id}", response_model=Film)
def get_film_details(film_id: int):
    """This method returns all the details of a film"""

    if Catalog.catalog_films is None:
        raise HTTPException(status_code=500, detail="Film catalog is not available")

    film = next((film for film in Catalog.catalog_films if film.id == film_id), None)

    if film is None:
        raise HTTPException(status_code=404, detail=f"Film with id {film_id} not found")

    return film


@app.post("/films/{film_id}/review")
def add_film_review(film_id: int, review: Review = Body(...)):
    """This method adds a review to a film"""

    if Catalog.catalog_films is None:
        raise HTTPException(status_code=500, detail="Film catalog is not available")

    film = next((film for film in Catalog.catalog_films if film.id == film_id), None)

    if film is None:
        raise HTTPException(status_code=404, detail=f"Film with id {film_id} not found")

    film.reviews.append(review)

    return {"message": "Review added successfully"}


@app.get("/films/{film_id}/reviews", response_model=List[Review])
def get_film_reviews(film_id: int):
    """This method returns all the reviews of a film"""

    if Catalog.catalog_films is None:
        raise HTTPException(status_code=500, detail="Film catalog is not available")

    film = next((film for film in Catalog.catalog_films if film.id == film_id), None)

    if film is None:
        raise HTTPException(status_code=404, detail=f"Film with id {film_id} not found")

    return film.reviews


@app.post("/users/{user_id}/watchlist")
def add_film_to_watchlist(user_id: int, film_id: Film.code = Body(...)):
    """This method adds a film to a user's watchlist"""

    if Catalog.users_registered is None or Catalog.catalog_films is None:
        raise HTTPException(
            status_code=500, detail="Users or film catalog is not available"
        )

    user = next((user for user in Catalog.users_registered if user.id == user_id), None)

    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    film = next(
        (film for film in Catalog.catalog_films if film.id == film_id.film_id), None
    )

    if film is None:
        raise HTTPException(
            status_code=404, detail=f"Film with id {film_id.film_id} not found"
        )

    user.watchlist.append(film)

    return {"message": "Film added to watchlist successfully"}

@app.post("/admin/films")
def add_film_to_catalog(film: Film = Body(...)):
    """This method adds a film to the catalog"""
    
    Catalog.catalog_films.append(film)

    return {"message": "Film added to catalog successfully"}