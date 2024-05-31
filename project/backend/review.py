"""
This file contains the class Review

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from pydantic import BaseModel
class Review(BaseModel):
    """
    This class control the behavior of the User class
    """

    username: str
    text: str
    likes: int
    replies: str
