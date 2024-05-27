import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # Solo necesitamos una instancia de FastAPI

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

engine = create_engine('postgresql://postgres:postgres@localhost:5432/public')
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

@app.get("/get_products")
def get_products():
    query = products.select()
    result = session.execute(query)
    product_list = result.fetchall()  # Cambiado el nombre de la variable a 'product_list' para evitar la confusión con la tabla 'products'
    return product_list

@app.post("/create_products") # Web services cannot be named the same because this could be an error
def create_product(name: str, description: str):
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)  # Cambiado el puerto a 8002