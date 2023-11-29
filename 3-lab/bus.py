from vehicle import Vehicle
from gas_tank import GasTank

class Bus(Vehicle):
    def __init__(self):
        print("Bus constructor call")
        super().__init__(GasTank(150))

    def __str__(self):
        return f"Bus: \n{super().__str__()}"
