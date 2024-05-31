"""
This file contains the class User

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from typing import List
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel
from db_connection import PostgresConnection
from film import Film
from review import Review


engine = create_engine('postgresql://ud_admin:Admin12345@localhost:5430/udproject2')
class User(BaseModel):
    """
    This class control the behavior of the User class
    """

    username: str
    password: str
    email: str
    name: str
    rated_films: List[Film]
    reviews: List[Review]
    replies: str
    fav_films: List[Film]
    watchlist: List[Film]

    def add_to_db(self):
        """
        This function adds a user to the database
        """
        connection = PostgresConnection(
            "ud_admin", "Admin12345", "localhost", "5430", "udproject2"
        )
        session = connection.session()
        user_db = UserDB(
            username=self.username,
            password=self.password,
            email=self.email,
            name=self.name,
            rated_films=self.rated_films,
            reviews=self.reviews,
            replies=self.replies,
            fav_films=self.fav_films,
            watchlist=self.watchlist,
        )
        session.add(user_db)
        session.commit()
        session.close()

    def login(self, username: str, password: str) -> bool:
        """
        This method logs in the user

        Args:
            username (str): the username of the user
            password (str): the password of the user
        """
        Session = sessionmaker(bind=engine) # pylint: disable=invalid-name
        session = Session()
        user_db = session.query(UserDB).filter_by(username=username, password=password).first()
        session.close()

        # If a user was found and the passwords match, return True
        if user_db is not None:
            return True
         # If no user was found or the passwords don't match, return False
        return False



    def has_watched_film(self, film: Film) -> bool:
        """
        This method checks if the user has watched a film

        Args:
            film (Film): the film to check
        """
        return film in self.rated_films

    def add_to_watchlist(self, film: Film):
        """
        This method adds a film to the user's watchlist

        Args:
            film (Film): the film to add
        """
        self.watchlist.append(film)

    def add_to_fav_films(self, film: Film):
        """
        This method adds a film to the user's favorite films

        Args:
            film (Film): the film to add
        """
        self.fav_films.append(film)

    def add_review(self, review: Review):
        """
        This method adds a review to the user's reviews

        Args:
            review (Review): the review to add
        """
        self.reviews.append(review)

    def get_watchlist(self) -> List[Film]:
        """
        This method returns the user's watchlist
        """
        return self.watchlist

    def get_fav_films(self) -> List[Film]:
        """
        This method returns the user's favorite films
        """
        return self.fav_films

    def get_reviews(self) -> List[Review]:
        """
        This method returns the user's reviews
        """
        return self.reviews
    
    class Config:
        """
        Pydantic configurarion for ORM mode
        """
        from_attributes = True


Base = declarative_base()


class UserDB(Base):
    """
    This class represents the behavior of the User in the database
    """

    __tablename__ = "users"

    username = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)
    rated_films = Column(String)
    reviews = Column(String)
    replies = Column(String)
    fav_films = Column(String)
    watchlist = Column(String)
