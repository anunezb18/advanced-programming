"""
This file contains the class Catalog

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from typing import List
from film import Film, FilmDB
from db_connection import PostgresConnection
from pydantic import BaseModel
from user import User

class Catalog(BaseModel):
    """This class represents a catalog of films"""

    catalog_films: List[Film] = []
    users_registered: List[User] = []

    @classmethod
    def show_all_films(cls):
        """
        This method returns the list of films in the catalog.

        Returns:
            List[Film]: list of films in the catalog

        """
        if len(cls.catalog_films) == 0:
            list_films = []
            connection = PostgresConnection(
                "ud_admin", "Admin12345", "localhost", 5432, "udproject"
            )
            for film_db in connection.session.query(FilmDB).all(): # pylint: disable=no-member
                film_obj = Film(
                    title=film_db.title,
                    code=film_db.code,
                    director=film_db.director,
                    year=film_db.year,
                    synopsis=film_db.synopsis,
                    ratings=film_db.ratings,
                    reviews=film_db.reviews,
                    lenght=film_db.lenght,
                    crew=film_db.crew,
                )
                list_films.append(film_obj)
            cls.catalog_films = list_films
        return cls.catalog_films

    @classmethod
    def add_videogame(cls, film: Film):
        """
        This method adds a film to the catalog list.

        Args:
            film (Film): film object to add
        """
        film.add_to_db()
        cls.catalog_films.append(film)

    @classmethod
    def update_film(cls, code: int, film: Film):
        """This method updates a film in the list based on its code"""
        for i in range(i(cls.catalog_films)):
            if cls.catalog_films[i].code == code:
                cls.catalog_films[i] = film
                break

    @classmethod
    def get_film(cls, code: int) -> Film:
        """This method perfoms a search by code"""
        for film in cls.catalog_films:
            if film.code == code:
                return film
        return None
