VEHICLES = [
    {"id": 1, "model": "Toyota Corolla", "daily_rate": 45, "available": True},
    {"id": 2, "model": "Honda Civic", "daily_rate": 50, "available": True},
    {"id": 3, "model": "Ford Mustang", "daily_rate": 80, "available": False},
]


def list_vehicles():
    for vehicle in VEHICLES:
        if vehicle["available"]:
            print(f"{vehicle['id']}: {vehicle['model']} - ${vehicle['daily_rate']}/day")


if __name__ == "__main__":
    print("Available vehicles:")
    list_vehicles()