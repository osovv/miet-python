from datetime import datetime
from exceptions import GasTankCapacityExceeded

class GasTank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.level = 0

    def refuel(self, liters, history):
        new_level = self.level + liters
        if new_level <= self.capacity:
            self.level = new_level
            history.add_record(datetime.now(), liters)
            return self.capacity - self.level
        else:
            raise GasTankCapacityExceeded(f"Cannot refuel {liters} liters: gas tank capacity exceeded for {self.level + liters - self.capacity} liters")


    def __str__(self):
        return f"Gas tank: {self.level}/{self.capacity} liters"
