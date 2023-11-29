from datetime import datetime

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
            print("Unable to refuel: gas tank capacity exceeded")

    def __str__(self):
        return f"Gas tank: {self.level}/{self.capacity} liters"
