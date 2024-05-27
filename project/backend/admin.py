"""
This file contains the class Admin

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""
from pydantic import BaseModel
from film import Film
from catalog import Catalog

class Admin(BaseModel):
    """This class control the behavior of the Admin class"""
    username: str
    password: str

    def add_film(self, film: Film):
        """This method adds a film to the catalog"""

        Catalog.catalog_films.append(film)

        return {"message": "Film added to catalog successfully"}
