"""
This file contains the class Rating

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""
from pydantic import BaseModel
class Rating(BaseModel):
    """
    This class control the behavior of the Rating class
    """
    username: str
    rating: float
