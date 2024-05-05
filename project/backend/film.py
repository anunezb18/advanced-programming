from typing import List
from pydantic import BaseModel

class Film(BaseModel):
    "This clas represents the behavior of film"
    title: str
    code: int
    director: str
    year: int
    synopsis: str
    ratings: str
    reviews: str
    lenght: str
    crew: List[str]
