"""
This file contains the class Film

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from db_connection import PostgresConnection
from rating import Rating
from review import Review


class Film(BaseModel):
    """This class represents the behavior of film"""

    title: str
    code: int
    director: str
    year: int
    synopsis: str
    ratings: List[Rating]
    reviews: List[Review]
    lenght: str
    crew: List[str]

    def add_to_db(self):
        """
        This function adds a film to the database
        """
        connection = PostgresConnection(
            "ud_admin", "Admin12345", "localhost", "5432", "udproject"
        )
        session = connection.session()
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
        session.add(film_db)
        session.commit()
        session.close()

    class Config:
        """
        Pydantic configurarion for ORM mode
        """
        from_attributes = True


Base = declarative_base()


class FilmDB(Base):
    """
    This class represents the behavior of the film in the database
    """

    __tablename__ = "films"

    title = Column(String)
    code = Column(Integer, primary_key=True)
    director = Column(String)
    year = Column(Integer)
    synopsis = Column(String)
    ratings = Column(String)
    reviews = Column(String)
    lenght = Column(String)
    crew = Column(String)
