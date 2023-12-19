# Define a simple class named 'Car'
class Car:
    # Class variable
    vehicle_type = "Automobile"

    # Constructor method
    def __init__(self, make, model, year):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year

    # Method to display information about the car
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating objects (instances) of the 'Car' class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2021)

# Accessing object attributes
print(f"Car 1: {car1.year} {car1.make} {car1.model}")
print(f"Car 2: {car2.year} {car2.make} {car2.model}")

# Accessing class variable
print(f"Car 1 Type: {car1.vehicle_type}")
print(f"Car 2 Type: {car2.vehicle_type}")

# Calling a method on objects
car1.display_info()
car2.display_info()
