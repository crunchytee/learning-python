class Vehicle:

    def __init__(self, make, model, fuel="gas") -> None:
        self.make = make
        self.model = model
        self.fuel = fuel
    def is_eco_friendly(self):
        if self.fuel == "gas":
            return True
        else: 
            return False

class Car(Vehicle):

    def __init__(self, make, model, fuel="gas", num_wheels=4) -> None:
        super().__init__(make, model, fuel=fuel)
        self.num_wheels = num_wheels