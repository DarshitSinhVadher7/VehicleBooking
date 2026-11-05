from flask import Flask, jsonify

app = Flask(__name__)

VEHICLES = [
    {"id": 1, "model": "Toyota Corolla", "daily_rate": 45, "available": True},
    {"id": 2, "model": "Honda Civic", "daily_rate": 50, "available": True},
    {"id": 3, "model": "Ford Focus", "daily_rate": 40, "available": False},
]

@app.get("/")
def home():
    return "Vehicle Rental API is running"

@app.get("/vehicles")
def list_vehicles():
    return jsonify(VEHICLES)

@app.get("/vehicles/available")
def available_vehicles():
    available = [vehicle for vehicle in VEHICLES if vehicle["available"]]
    return jsonify(available)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
