"""
This file contains the class Rating

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""
from pydantic import BaseModel
from film import Film
from user import User

class Rating(BaseModel):
    """
    This class control the behavior of the Rating class
    """
    user: User
    film_rated: Film
    rating: float

    def validate_user_for_rating(self, user: User):
        """
        This function validates if a user can rate a film

        Args:
            user (User): the user to validate

        Returns:
            bool: True if the user can rate a film, False otherwise
        """
        if not user.is_logged_in() is False:
            return False

        if not user.has_watched_film() is False:
            return False
        return True