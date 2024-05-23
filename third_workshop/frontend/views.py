def vehicles_list(request):
    vehicles_list = [
        {
        "vehicles": [
        {
        "type": "Car",
        "engine": {
            "type": "Gasoline",
            "potency": 2000,
            "weight": 150
        },
        "chasis": "A",
        "model": "Civic",
        "year": 2022
        },
        {
        "type": "Car",
        "engine": {
            "type": "Diesel",
            "potency": 2500,
            "weight": 50
        },
        "chasis": "B",
        "model": "Accord",
        "year": 2021
        },
        {
        "type": "Car",
        "engine": {
            "type": "Electric",
            "potency": 5000,
            "weight": 35
        },
        "chasis": "B",
        "model": "Model S",
        "year": 2023
        },
        {
        "type": "Truck",
        "engine": {
            "type": "Diesel",
            "potency": 3500,
            "weight": 250
        },
        "chasis": "B",
        "model": "F-150",
        "year": 2020
        },
        {
        "type": "Truck",
        "engine": {
            "type": "Diesel",
            "potency": 4500,
            "weight": 300
        },
        "chasis": "B",
        "model": "Silverado",
        "year": 2019
        },
        {
        "type": "Truck",
        "engine": {
            "type": "Gasoline",
            "potency": 4000,
            "weight": 350
        },
        "chasis": "A",
        "model": "Ram 1500",
        "year": 2021
        },
        {
        "type": "Yacht",
        "engine": {
            "type": "Diesel",
            "potency": 6000,
            "weight": 500
        },
        "chasis": "B",
        "model": "Sunseeker 76",
        "year": 2018
        },
        {
        "type": "Yacht",
        "engine": {
            "type": "Diesel",
            "potency": 8000,
            "weight": 600
        },
        "chasis": "A",
        "model": "Princess 68",
        "year": 2020
        },
    ]
    }

    ]

def engines_list(request):
    engines_list = [
        {
            "type": "Gasoline",
            "potency": 2000,
            "weight": 150
        },
        {
            "type": "Diesel",
            "potency": 2500,
            "weight": 50
        },
        {
            "type": "Electric",
            "potency": 5000,
            "weight": 35
        }
    ]

def vehicles_to_add(request):
    vehicles_list = [
        {
        "type": "Yacht",
        "engine": {
            "type": "Diesel",
            "potency": 7000,
            "weight": 650
        },
        "chasis": "B",
        "model": "Ferretti 960",
        "year": 2019
        },
        {
        "type": "Motorcycle",
        "engine": {
            "type": "Gasoline",
            "potency": 1000,
            "weight": 110
        },
        "chasis": "A",
        "model": "CBR1000RR",
        "year": 2022
        },
        {
        "type": "Motorcycle",
        "engine": {
            "type": "Gasoline",
            "potency": 900,
            "weight": 200
        },
        "chasis": "B",
        "model": "GSX-R1000",
        "year": 2021
        },
        {
        "type": "Motorcycle",
        "engine": {
            "type": "Gasoline",
            "potency": 1200,
            "weight": 100
        },
        "chasis": "B",
        "model": "S1000RR",
        "year": 2023
        }
    ]

