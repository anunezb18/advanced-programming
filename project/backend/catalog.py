"""
This file contains the class Catalog

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from film import Film

class Catalog:
    """This class represents a catalog of films"""

    catalog_films = []

    @classmethod
    def show_films(cls):
        """This method shows all films in the application

        Returns:
            list: the list of films.
        """
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
                cls.catalog_films[i] = Film
                break

    @classmethod
    def get_film(cls, code: int) -> Film:
        """This method perfoms a search by code"""
        for film in cls.catalog_films:
            if film.code == code:
                return film
        return None
