# Base class
class Shape:
    def area(self):
        pass  # Abstract method, to be overridden by subclasses

# Derived class 1
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    # Overriding the area method
    def area(self):
        return self.side_length ** 2

# Derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the area method
    def area(self):
        return 3.14 * self.radius ** 2

# Function demonstrating polymorphism
def print_area(shape):
    print(f"Area: {shape.area()}")

# Creating instances of the derived classes
square = Square(5)
circle = Circle(3)

# Using polymorphism in the print_area function
print_area(square)  # Output: Area: 25
print_area(circle)  # Output: Area: 28.26
