class History:
    def __init__(self):
        self.refueling_history = []

    def add_record(self, date_time, liters):
        self.refueling_history.append((date_time, liters))
        self.refueling_history = self.refueling_history[-10:]

    def read(self):
        return self.refueling_history


    def __str__(self):
        return f"Refueling history: {self.refueling_history}"
