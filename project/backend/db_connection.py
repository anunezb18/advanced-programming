"""
This file contains the clas for connect into the database

@Author: <mdpilarp@udistrital.edu.co>
<anunezb@udistrital.edu.co>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresConnection:
    """
    This class is used to connect to the database
    """
    def __init__(
        self, user: str, password: str, host: str, port: int, database_name: str
    ):
        self.engine = create_engine(
            f"postgresql://{user}:{password}@{host}:{port}/{database_name}"
        )
        self.session = sessionmaker(bind=self.engine)
