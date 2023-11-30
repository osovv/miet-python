from bus import Bus
from passenger_car import PassengerCar
from exceptions import GasTankCapacityExceeded
import pickle

def save_data_to_file(data, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f"Error saving a file: {e}")

def load_data_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error reading a file: {e}")

def input_fuel_amount(vehicle_name):
    while True:
        try:
            amount = int(input(f"Enter amount of fuel to refuel {vehicle_name} (liters): "))
            if amount <= 0:
                raise ValueError("Fuel amount cannot be non-positive")
            return amount
        except ValueError as e:
            print(f"Incorrent input: {e}")

def main():
  bus = Bus()
  try:
    bus_fuel = input_fuel_amount("a bus")
    bus.refuel(bus_fuel)
  except GasTankCapacityExceeded as e:
    print(e)
    return
  print(bus)

  car = PassengerCar()
  try:
    car_fuel = input_fuel_amount("a passenger car")
    car.refuel(car_fuel)
  except GasTankCapacityExceeded as e:
    print(e)
    return
  print("Car < Bus ?", car < bus)

  print("Saving data to the file...")
  save_data_to_file({"bus": bus, "car": car}, "vehicles.dat")

  print("Loading data from the file...")
  loaded_data = load_data_from_file("vehicles.dat")
  if loaded_data:
      print("Loaded bus:\n", loaded_data["bus"])
      print("Loaded passenger car:\n", loaded_data["car"])


if __name__ == "__main__":
  main()
