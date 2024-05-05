"""
This file contains the class User

@Author: mdpilarp@udistrital.edu.co
anunezb@udistrital.edu.co
"""
from pydantic import BaseModel
class User(BaseModel):
    """
    This class control the behavior of the User class
    """
    username: str
    password: str
    email: str
    name: str
    rated_films: str
    reviews: str
    replies: str
    fav_films: str
    watchlist: str

    def login(self, username: str, password: str):
        """
        This method is used to login into the application

        Args:
            username (str): the alias of the user
            password (str): the password of the user
        """
        # TODO finish the function
        return True or False