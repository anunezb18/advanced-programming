"""
This file contains the class Review

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from pydantic import BaseModel
from film import Film
from user import User


class Review(BaseModel):
    """
    This class control the behavior of the User class
    """

    user: User
    film_reviewed: Film
    text: str
    likes: int
    replies: str

    def validate_user_for_review(self, user: User):
        """
        This function validates if a user can make a review

        Args:
            user (User): the user to validate

        Returns:
            bool: True if the user can make a review, False otherwise
        """
        if not user.is_logged_in() is False:
            return False

        if not user.has_watched_film() is False:
            return False
        return True
