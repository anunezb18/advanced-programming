"""This module an internal platform  of a vehicle constructor company"""

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

class Car(Vehicle):
    """
    This is a subclass of vehicle and it is to create a car object
    """

    def __init__( self,engine: Engine, chasis: str,model, year: int,brand,passenger_capacity, trunk_capacity,):
        super().__init__(engine, chasis, model, year)
        self.brand = brand
        self.passenger_capacity = passenger_capacity
        self.trunk_capacity = trunk_capacity
    
    def __str__(self):
        return f"Car -> {super().__str__()}, Brand: {self.brand}, Passenger Capacity: {self.passenger_capacity}, Trunk Capacity: {self.trunk_capacity}"

class Truck(Vehicle):
    """
    This is a subclass of vehicle and it is to create a truck object
    """

    def __init__(self, engine: Engine, chasis: str, model, year: int, charge_capacity, height):
        super().__init__(engine, chasis, model, year)
        self.charge_capacity = charge_capacity
        self.height = height
    
    def __str__(self):
        return f"Truck -> {super().__str__()}, Charge Capacity: {self.charge_capacity}, Height: {self.height}"


class Yacht(Vehicle):
    """
    This is a subclass of vehicle and it is to create a yatch object
    """

    def __init__(self, engine: Engine, chasis: str, model, year: int, lenght, passenger_capacity):
        super().__init__(engine, chasis, model, year)
        self.lenght = lenght
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f"Yacht -> {super().__str__()}, Length: {self.lenght}, Passenger Capacity: {self.passenger_capacity}"


class Motorcycle(Vehicle):
    """
    This is a subclass of vehicle and it is to create a motorcycle object
    """

    def __init__(self, engine: Engine, chasis: str, model, year: int, brand, cylinder_capacity):
        super().__init__(engine, chasis, model, year)
        self.brand = brand
        self.cylinder_capacity = cylinder_capacity

    def __str__(self):
        return f"Motorcycle -> {super().__str__()}, Brand: {self.brand}, Cylinder Capacity: {self.cylinder_capacity})"

def create_engine():
    """
    This is for create an engine
    """
    etype = input("Enter engine type: ")
    potency = float(input("Enter engine potency: "))
    weight = float(input("Enter engine weight: "))

    return Engine(etype, potency, weight)

def create_vehicle(vehicle_type):
    """
    Function to create a new vehicle
    """
    engine = create_engine()
    chasis = input("Enter chasis (A/B): ")
    model = input("Enter vehicle model: ")
    year = input("Enter vehicle year: ")

    if vehicle_type == "Car":
        brand = input("Enter car brand: ")
        passenger_capacity = input("Enter passenger capacity: ")
        trunk_capacity = input("Enter trunk capacity: ")
        return Car(engine, chasis, model, year, brand, passenger_capacity, trunk_capacity)
  
    elif vehicle_type == "Truck":
        charge_capacity = input("Enter truck charge capacity: ")
        height = input("Enter truck height: ")
        return Truck(engine, chasis, model, year, charge_capacity, height)

    elif vehicle_type == "Yacht":
        length = input("Enter yacht length: ")
        passenger_capacity = input("Enter passenger capacity: ")
        return Yacht(engine, chasis, model, year, length, passenger_capacity)

    elif vehicle_type == "Motorcycle":
        brand = input("Enter motorcycle brand: ")
        cylinder_capacity = input("Enter cylinder capacity: ")
        return Motorcycle(engine, chasis, model, year, brand, cylinder_capacity)

def main():
    """
    This is the function that runs the menus
    """
    while True:
        print("\nVehicle Constructor Program")
        print("1. Create Car")
        print("2. Create Truck")
        print("3. Create Yacht")
        print("4. Create Motorcycle")
        print("5. See registred vehicles")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            vehicle = create_vehicle("Car")
            print(vehicle)
            list_vehicles.append(vehicle)
        elif choice == "2":
            vehicle = create_vehicle("Truck")
            print(vehicle)
            list_vehicles.append(vehicle)
        elif choice == "3":
            vehicle = create_vehicle("Yacht")
            print(vehicle)
            list_vehicles.append(vehicle)
        elif choice == "4":
            vehicle = create_vehicle("Motorcycle")
            print(vehicle)
            list_vehicles.append(vehicle)
        elif choice == "5":
            print()
            for elem in list_vehicles:
                print(elem)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

list_vehicles = []
main()