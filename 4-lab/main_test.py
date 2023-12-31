import unittest
from bus import Bus
from passenger_car import PassengerCar
from exceptions import GasTankCapacityExceeded
from main import save_data_to_file, load_data_from_file
import os

class TestVehicleManagementSystem(unittest.TestCase):
    def setUp(self):
        self.bus = Bus()
        self.car = PassengerCar()

    def test_bus_refuel(self):
        self.bus.refuel(50)
        self.assertEqual(self.bus.gas_tank.level, 50)

    def test_car_refuel(self):
        self.car.refuel(30)
        self.assertEqual(self.car.gas_tank.level, 30)

    def test_gas_tank_capacity_exceeded(self):
        with self.assertRaises(GasTankCapacityExceeded):
            self.bus.refuel(1000)  # Assuming this exceeds the capacity

    def test_save_and_load_data(self):
        test_data = {"bus": self.bus, "car": self.car}
        filename = "test_vehicles.dat"
        save_data_to_file(test_data, filename)
        self.assertTrue(os.path.exists(filename))
        loaded_data = load_data_from_file(filename)
        self.assertEqual(loaded_data["bus"].gas_tank.level, self.bus.gas_tank.level)
        self.assertEqual(loaded_data["car"].gas_tank.level, self.car.gas_tank.level)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
