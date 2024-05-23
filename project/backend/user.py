"""
This file contains the class User

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from typing import List
from catalog import Catalog
from film import Film
from pydantic import BaseModel
from review import Review


class User(BaseModel):
    """
    This class control the behavior of the User class
    """

    username: str
    password: str
    email: str
    name: str
    rated_films: List[Film]
    reviews: List[Review]
    replies: str
    fav_films: List[Film]
    watchlist: List[Film]

    def login(self, username: str, password: str) -> bool:
        """
        This method is used to login into the application

        Args:
            username (str): the alias of the user
            password (str): the password of the user
        """
        for user in Catalog.users_registered:
            if user.username == username and user.password == password:
                return True
        return False

    def is_logged_in(self):
        """
        This method checks if the user is logged in
        """
        return self in Catalog.users_registered

    def has_watched_film(self, film: Film) -> bool:
        """
        This method checks if the user has watched a film

        Args:
            film (Film): the film to check
        """
        return film in self.rated_films

    def add_to_watchlist(self, film: Film):
        """
        This method adds a film to the user's watchlist

        Args:
            film (Film): the film to add
        """
        self.watchlist.append(film)

    def add_to_fav_films(self, film: Film):
        """
        This method adds a film to the user's favorite films

        Args:
            film (Film): the film to add
        """
        self.fav_films.append(film)

    def add_review(self, review: Review):
        """
        This method adds a review to the user's reviews

        Args:
            review (Review): the review to add
        """
        self.reviews.append(review)

    def get_watchlist(self) -> List[Film]:
        """
        This method returns the user's watchlist
        """
        return self.watchlist

    def get_fav_films(self) -> List[Film]:
        """
        This method returns the user's favorite films
        """
        return self.fav_films

    def get_reviews(self) -> List[Review]:
        """
        This method returns the user's reviews
        """
        return self.reviews
