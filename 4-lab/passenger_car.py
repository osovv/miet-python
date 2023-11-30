from vehicle import Vehicle
from gas_tank import GasTank

class PassengerCar(Vehicle):
    def __init__(self):
        super().__init__(GasTank(50))

    def __str__(self):
        return f"Passenger car: \n{super().__str__()}"
