from history import History

class Vehicle:
    def __init__(self, gas_tank):
        print("Vehicle constructor call")
        self.gas_tank = gas_tank
        self.history = History()

    def refuel(self, liters):
        self.gas_tank.refuel(liters, self.history)

    def read_refueling_history(self):
        return self.history.read()

    def __str__(self):
        return f"Vehicle: \n{self.gas_tank}\n{self.history}"

    def __lt__(self, other):
        return self.gas_tank.capacity < other.gas_tank.capacity
