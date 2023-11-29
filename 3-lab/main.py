from bus import Bus
from passenger_car import PassengerCar
def main():
  bus = Bus()
  bus.refuel(100)
  print(bus)
  car = PassengerCar()
  car.refuel(40)
  print(car)
  print("Car < Bus ?", car < bus)


if __name__ == "__main__":
  main()
