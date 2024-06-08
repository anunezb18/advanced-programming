"""
This file contains the class Review

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from typing import List, Optional
from pydantic import BaseModel
from reply import Reply


class Review(BaseModel):
    """This class represents the behavior of review"""

    username: str
    text: str
    likes: Optional[int] = None
    replies: Optional[List[Reply]] = None
