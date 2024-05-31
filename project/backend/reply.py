"""
This file contains the class Reply

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from pydantic import BaseModel
class Reply(BaseModel):
    """
    This class control the behavior of the Reply class
    """

    username: str
    text: str
    date: str
    likes: int
