"""
This file contains the class Reply

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from pydantic import BaseModel
from review import Review
from user import User


class Reply(BaseModel):
    """
    This class control the behavior of the Reply class
    """

    user: User
    review_replied: Review
    text: str
    date: str
    likes: int
