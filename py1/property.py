class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def radius(self):
        print("Getting radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            print("Setting radius")
            self._radius = value
        else:
            print("Invalid radius value. Must be greater than 0.")

# Creating an instance of the Circle class
circle = Circle(5)

# Using the property
print(circle.radius)  # Output: Getting radius

# Using the setter through the property
circle.radius = 8    # Output: Setting radius

# Attempting to set an invalid value
circle.radius = -2   # Output: Invalid radius value. Must be greater than 0.
