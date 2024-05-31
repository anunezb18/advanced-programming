"""
This file contains the class Admin

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from film import FilmDB

engine = create_engine('postgresql://ud_admin:Admin12345@localhost:5432/udproject')
class Admin(BaseModel):
    """This class control the behavior of the Admin class"""
    username: str
    password: str

    def add_film(self, title, code, director, year, synopsis, lenght, crew):
        """This method adds a film by the admin to the database"""

        new_film = FilmDB(title=title,
            code=code,
            director=director,
            year=year,
            synopsis=synopsis,
            ratings=None,
            reviews=None,
            lenght=lenght,
            crew=crew,)
        
        Session = sessionmaker(bind=engine) # pylint: disable=invalid-name
        session = Session()

        session.add(new_film)
        session.commit()

        return {"message": "Film added to catalog successfully"}
