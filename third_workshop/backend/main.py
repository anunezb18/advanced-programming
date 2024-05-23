from fastapi import FastAPI 
from typing import List
from application import Vehicle, Engine

app = FastAPI()

@app.post("/add_vehicle")
def add_vehicle(vehicle: Vehicle):
    """
    This method lets add a new vehicle

    Args:
        vehicle (Vehicle): vehicle to be added
    """
    return vehicle.add_vehicle(vehicle)

@app.post("/see_vehicles")
def see_vehicles(list_vehicles: List[Vehicle]):
    """
    This method lets see the catalog of vehicles

    Args:
        list_vehicles: List[Vehicle]: list of vehicles to watch
    """
    return list_vehicles

@app.post("/see_engines")
def see_engines(list_engines: List[Engine]):
    """
    This method lets see the catalog of engines

    Args:
        list_engines: List[Engines]: list of engines to watch
    """
    return list_engines
