"""This module an internal platform  of a vehicle constructor company"""

# ------------------------------------Class Engine-----------------------------------

class Engine:
    """
    This is a class about a vehicle's engine

    """

    def __init__(self, etype: str, potency, weight: float):
        self.type = etype
        self.potency = potency
        self.weight = weight

    def __str__(self):
        return f"(Type: {self.type}, Potency: {self.potency}, Weight: {self.weight})"

# ------------------------------------Class Vehicle-----------------------------------
class Vehicle:
    """
    This is the superclass Vehicle, it is about any means of transport
    """

    def __init__(self, engine: Engine, chasis: str, model, year: int):
        self.engine = engine
        self.chasis = chasis
        self.model = model
        self.gas_consumption = self.calculate_consumption()
        self.year = year

    def calculate_consumption(self):
        """
        This function allows us to calculate the gas consumption of each vehicle

        Returns:
            gas_consumption = float
        """
        if self.chasis == "A":
            gas_consumption = 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.3
        elif self.chasis == "B":
            gas_consumption = 1.1 * self.engine.potency + 0.2 * self.engine.weight - 0.5
        else:
            gas_consumption = None
        return gas_consumption

    def __str__(self):
        return f"Engine: {self.engine}, Chasis: {self.chasis}, Model: {self.model}, Gas Consumption: {self.gas_consumption}, Year: {self.year}"


# ------------------------------------Classes of Vehicle-----------------------------------
class Car(Vehicle):
    """
    This is a subclass of vehicle and it is to create a car object
    """

    def __init__(
        self,
        engine: Engine,
        chasis: str,
        model,
        year: int,
    ):
        super().__init__(engine, chasis, model, year)

    def __str__(self):
        return f"Car -> {super().__str__()}"


class Truck(Vehicle):
    """
    This is a subclass of vehicle and it is to create a truck object
    """

    def __init__(
        self, engine: Engine, chasis: str, model, year: int
    ):
        super().__init__(engine, chasis, model, year)

    def __str__(self):
        return f"Truck -> {super().__str__()}"


class Yacht(Vehicle):
    """
    This is a subclass of vehicle and it is to create a yatch object
    """

    def __init__(
        self, engine: Engine, chasis: str, model, year: int
    ):
        super().__init__(engine, chasis, model, year)

    def __str__(self):
        return f"Yacht -> {super().__str__()}"


class Motorcycle(Vehicle):
    """
    This is a subclass of vehicle and it is to create a motorcycle object
    """

    def __init__(
        self, engine: Engine, chasis: str, model, year: int
    ):
        super().__init__(engine, chasis, model, year)

    def __str__(self):
        return f"Motorcycle -> {super().__str__()}"
    
#----------------------------------------------Class Admin & Client----------------------------------------------
class Admin:
    """
    This is a class for the manager
    """
    def __init__(self):
        self.username = "admin123"
        self.password = "imtheboss"
    
    def add_vehicle(self, vehicle: Vehicle):
        """
        This is a function to add a vehicle by the admin
        """
        list_vehicles.append(vehicle)

class Client:
    """
    This is a class for client
    """
    def __init__(self):
        pass

    def set_aside(self, emodel, eyear):
        """
        This a function for set aside a vehicle by the client
        """
        for elem in list_vehicles:
            if isinstance(elem, Vehicle):
                if elem.model == emodel and elem.year == eyear:
                    list_vehicles.remove(elem)
                    print("Thank you, You sucessfully set aside the vehicle")
                else:
                    pass

    def search_vehicle(self, model: str):
        """
        Function for search a vehicle on the list
        """
        for elem in list_vehicles:
            if isinstance(elem, Vehicle):
                if elem.model == model:
                    print("•", elem)
                else:print("Vehicle not found")
            
    def show_car(self):
        """
        Function for show car
        """
        for elem in list_vehicles:
            if isinstance(elem, Car):
                print("•", elem)
    
    def show_moto(self):
        """
        Function for show motorcycles
        """
        for elem in list_vehicles:
            if isinstance(elem, Motorcycle):
                print("•", elem)

    def show_truck(self):
        """
        Function for show trucks
        """
        for elem in list_vehicles:
            if isinstance(elem, Truck):
                print("•", elem)
    
    def show_yacht(self):
        """
        Function for show yachts
        """
        for elem in list_vehicles:
            if isinstance(elem, Yacht):
                print("•", elem)

# ----------------------------Functions to create a Vehicle or an Engine---------------------------
def create_engine():
    """
    This is for create an engine
    """
    try:
        etype = input("Enter engine type: ")
        potency = float(input("Enter engine potency: "))
        weight = float(input("Enter engine weight: "))
    except ValueError:
        potency = 0
        weight = 0

    return Engine(etype, potency, weight)


def create_vehicle(vehicle_type):
    """
    Function to create a new vehicle
    """
    engine = create_engine()
    chasis = input("Enter chasis (A/B): ")
    model = input("Enter vehicle model: ")
    year = input("Enter vehicle year: ")

list_vehicles = [
    Car(Engine("Gasoline", 2000,150), "A", "Civic", 2022),
    Car(Engine("Diesel", 2500,50), "B", "Accord", 2021),
    Car(Engine("Electric", 5000,35), "B", "Model S", 2023),
    Truck(Engine("Diesel", 3500, 250), "B", "F-150", 2020),
    Truck(Engine("Diesel", 4500, 300), "B", "Silverado", 2019),
    Truck(Engine("Gasoline", 4000, 350), "A", "Ram 1500", 2021),
    Yacht(Engine("Diesel", 6000,500), "B", "Sunseeker 76", 2018),
    Yacht(Engine("Diesel", 8000,600), "A", "Princess 68", 2020),
    Yacht(Engine("Diesel", 7000,650), "B", "Ferretti 960", 2019),
    Motorcycle(Engine("Gasoline", 1000, 110), "A", "CBR1000RR", 2022),
    Motorcycle(Engine("Gasoline", 900, 200), "B", "GSX-R1000", 2021),
    Motorcycle(Engine("Gasoline", 1200,100), "B", "S1000RR", 2023)
]
