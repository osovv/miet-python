class GasTankCapacityExceeded(Exception):
    def __init__(self, message="Gas tank capacity exceeded"):
        self.message = message
        super().__init__(self.message)
