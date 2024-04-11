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
        brand,
        passenger_capacity,
        trunk_capacity,
    ):
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

    def __init__(
        self, engine: Engine, chasis: str, model, year: int, charge_capacity, height
    ):
        super().__init__(engine, chasis, model, year)
        self.charge_capacity = charge_capacity
        self.height = height

    def __str__(self):
        return f"Truck -> {super().__str__()}, Charge Capacity: {self.charge_capacity}, Height: {self.height}"


class Yacht(Vehicle):
    """
    This is a subclass of vehicle and it is to create a yatch object
    """

    def __init__(
        self, engine: Engine, chasis: str, model, year: int, lenght, passenger_capacity
    ):
        super().__init__(engine, chasis, model, year)
        self.lenght = lenght
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f"Yacht -> {super().__str__()}, Length: {self.lenght}, Passenger Capacity: {self.passenger_capacity}"


class Motorcycle(Vehicle):
    """
    This is a subclass of vehicle and it is to create a motorcycle object
    """

    def __init__(
        self, engine: Engine, chasis: str, model, year: int, brand, cylinder_capacity
    ):
        super().__init__(engine, chasis, model, year)
        self.brand = brand
        self.cylinder_capacity = cylinder_capacity

    def __str__(self):
        return f"Motorcycle -> {super().__str__()}, Brand: {self.brand}, Cylinder Capacity: {self.cylinder_capacity})"
    
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

    if vehicle_type == "Car":
        brand = input("Enter car brand: ")
        passenger_capacity = input("Enter passenger capacity: ")
        trunk_capacity = input("Enter trunk capacity: ")
        return Car(
            engine, chasis, model, year, brand, passenger_capacity, trunk_capacity
        )

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

# ------------------------------------Menu-----------------------------------
def main():
    """
    This is the function that runs the menu
    """
    while True:
        print("\nCar Company Application")
        print("1. Enter as admin")
        print("2. Enter as client")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            e_username = input("Enter the username: ")
            e_password = input("Enter the password: ")
            if e_username == "admin123" and e_password == "imtheboss":
                menu_admin()
            else:
                print("The password or username are incorrent. Please try again.")
        elif choice == "2":
            menu_client()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def menu_admin():
    """
    This is the menu for the managers
    """
    while True:
        admin = Admin()
        print()
        print("Welcome to the manager mode. This are the following options.")
        print("1. Add new vehicles")
        print("2. See existing vehicles")
        print("3. Exit")
        choice_2 = input("Enter your choice (1-3): ")
        if choice_2 == "1":
            print("What type of vehicle do you want to add to the catalog?")
            print("1. Car")
            print("2. Motorcycle")
            print("3. Truck")
            print("4. Yatch")
            print("5. Exit")
            choice_3 = input("Enter your choice (1-5): ")
            if choice_3 == "1":
                vehicle = create_vehicle("Car")
                print(vehicle)
                admin.add_vehicle(vehicle)
            elif choice_3 == "2":
                vehicle = create_vehicle("Motorcycle")
                print(vehicle)
                admin.add_vehicle(vehicle)
            elif choice_3 == "3":
                vehicle = create_vehicle("Truck")
                print(vehicle)
                admin.add_vehicle(vehicle)
            elif choice_3 == "4":
                vehicle = create_vehicle("Yacht")
                print(vehicle)
                admin.add_vehicle(vehicle)
            elif choice_3 == "5":
                print("Goodbye!")
                break
        elif choice_2 == "2":
            print()
            for elem in list_vehicles:
                print("•", elem)       
        elif choice_2 == "3":
            print("Goodbye!")
            break

def menu_client():
    """
    This is the menu for the clients
    """
    while True:
        client = Client()
        print()
        print("Welcome to the client mode. This are the following options.")
        print("1. See existing vehicles")
        print("2. Search vehicle by model")
        print("3. Filter vehicles by type")
        print("4. Set aside a vehicle")
        print("5. Exit")
        choice_4 = input("Enter your choice (1-5): ")
        if choice_4 == "1":
            print()
            for elem in list_vehicles:
                print("•", elem)
        elif choice_4 == "2":
            model = input("Enter the model of the vehicle you are looking for: ")
            client.search_vehicle(model)
        elif choice_4 == "3":
            print("What type of vehicle do you want to watch?")
            print("1. Car")
            print("2. Motorcycle")
            print("3. Truck")
            print("4. Yatch")
            print("5. Exit")
            choice_5 = input("Enter your choice (1-5): ")
            print()
            if choice_5 == "1":
                client.show_car()
            elif choice_5 == "2":
                client.show_moto()
            elif choice_5 == "3":
                client.show_truck()
            elif choice_5 == "4":
                client.show_yacht()
            elif choice_5 == "5":
                print("Goodbye!")
                break
        elif choice_4 == "4":
            emodel = input("Enter the model of the vehicle you want: ")
            eyear = input("Enter the year of the vehicle you want: ")
            client.set_aside(emodel, eyear)
        elif choice_4 == "5":
            print("Goodbye!")
            break

list_vehicles = [
    Car(Engine("Gasoline", 2000,150), "ABC123", "Civic", 2022, "Honda", 5, 500),
    Car(Engine("Diesel", 2500,50), "DEF456", "Accord", 2021, "Honda", 5, 550),
    Car(Engine("Electric", 5000,35), "GHI789", "Model S", 2023, "Tesla", 5, 600),
    Truck(Engine("Diesel", 3500, 250), "XYZ123", "F-150", 2020, 3000, 2.5),
    Truck(Engine("Diesel", 4500, 300), "UVW456", "Silverado", 2019, 3500, 2.7),
    Truck(Engine("Gasoline", 4000, 350), "RST789", "Ram 1500", 2021, 3200, 2.6),
    Yacht(Engine("Diesel", 6000,500), "IJK123", "Sunseeker 76", 2018, 23, 10),
    Yacht(Engine("Diesel", 8000,600), "LMN456", "Princess 68", 2020, 21, 8),
    Yacht(Engine("Diesel", 7000,650), "OPQ789", "Ferretti 960", 2019, 29, 12),
    Motorcycle(Engine("Gasoline", 1000, 110), "ABC001", "CBR1000RR", 2022, "Honda", 1000),
    Motorcycle(Engine("Gasoline", 900, 200), "DEF002", "GSX-R1000", 2021, "Suzuki", 999),
    Motorcycle(Engine("Gasoline", 1200,100), "GHI003", "S1000RR", 2023, "BMW", 999)
]


if __name__ == "__main__":
    main()
