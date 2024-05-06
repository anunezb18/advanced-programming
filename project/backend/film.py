"""
This file contains the class User

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db_connection import PostgresConnection


class Film(BaseModel):
    """This class represents the behavior of film"""

    title: str
    code: int
    director: str
    year: int
    synopsis: str
    ratings: str
    reviews: str
    lenght: str
    crew: List[str]

    def __init__(self):
        self.connection = PostgresConnection(
            "ud_ap_user", "P4$$w0rd", "localhost", 5432, "ud_ad_project"
        )

    def add_to_db(self):
        session = self.connection.session()
        film_db = FilmDB(
            title=self.title,
            code=self.code,
            director=self.director,
            year=self.year,
            synopsis=self.synopsis,
            ratings=self.ratings,
            reviews=self.reviews,
            lenght=self.lenght,
            crew=self.crew,
        )

        self.session.add(film_db)
        self.session.commit()
        self.session.close()
    
    class Config:
        orm_mode = True

Base = declarative_base()

class FilmDB(Base):
    __tablename__ = "films"

    title = Column(String)
    code = Column(Integer, primary_key=True)    
    director = Column(String)
    year = Column(Integer)
    synopsis = Column(String)
    ratings = Column(String)
    reviews = Column(String)
    lenght = Column(str)
    crew = Column(List[String])

print("Example")