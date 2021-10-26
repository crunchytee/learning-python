class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        print(f"New car!")
        self.name = name

    def __str__(self) -> str:
        return f"My car the {self.name} currently {self.runs}"

    def __repr__(self) -> str:
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} is broken. Oh no!")
    
    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels