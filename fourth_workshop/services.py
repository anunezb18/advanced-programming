"""This modyule contains the code for the FastAPI web service."""

# Se ha documentado el codigo, ya que faltaba
# Se creó el entorno virtual para instalar las librerias requeridas

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()  # Solo necesitamos una instancia de FastAPI

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]


class Product(BaseModel):
    """Class to represent a product."""
    id: int
    name: str
    description: str


# Se ha añadido el middleware para permitir el acceso a la API desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello_ud")
def hello_ud():
    """This function return a welcome message."""
    return "Welcome to UD!"


engine = create_engine("postgresql://postgres:postgres@localhost:5432/public")
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
)


@app.get("/get_products")
def get_products():
    """This function returns the list of products."""
    query = products.select()
    result = session.execute(query)
    # Cambiado el nombre de la variable a 'product_list' para evitar confusión con tabla 'products'
    product_list = result.fetchall()
    if not product_list:
        return {"message": "No products found"}
    return product_list


@app.post("/create_products")
# Los servicios web estaban llamados igual por lo cual se cambió esto
def create_product(product: Product):
    """This function creates a new product."""
    # Aqui faltaba añadir el id del producto como parametro
    query = products.insert().values(
        id=product.id, name=product.name, description=product.description
    )  # pylint: disable=line-too-long
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)  # Cambiado el puerto a 8002
