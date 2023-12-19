from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, to be implemented by subclasses

    @abstractmethod
    def display_info(self):
        pass  # Abstract method, to be implemented by subclasses

# Concrete subclass 1
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    # Implementing the abstract methods
    def area(self):
        return self.side_length ** 2

    def display_info(self):
        print(f"Square - Side Length: {self.side_length}")

# Concrete subclass 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the abstract methods
    def area(self):
        return 3.14 * self.radius ** 2

    def display_info(self):
        print(f"Circle - Radius: {self.radius}")

# Function demonstrating abstraction
def print_shape_info(shape):
    shape.display_info()
    print(f"Area: {shape.area()}")

# Creating instances of the concrete subclasses
square = Square(5)
circle = Circle(3)

# Using abstraction in the print_shape_info function
print_shape_info(square)
print("\n")  # Adding a newline for better separation
print_shape_info(circle)
