class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter method for width
    def get_width(self):
        print("Getting width")
        return self._width

    # Setter method for width
    def set_width(self, value):
        if value > 0:
            print("Setting width")
            self._width = value
        else:
            print("Invalid width value. Must be greater than 0.")

    # Getter method for height
    def get_height(self):
        print("Getting height")
        return self._height

    # Setter method for height
    def set_height(self, value):
        if value > 0:
            print("Setting height")
            self._height = value
        else:
            print("Invalid height value. Must be greater than 0.")

# Creating an instance of the Rectangle class
rectangle = Rectangle(4, 6)

# Using getters and setters
print(rectangle.get_width())    # Output: Getting width
rectangle.set_width(8)          # Output: Setting width

print(rectangle.get_height())   # Output: Getting height
rectangle.set_height(10)        # Output: Setting height

# Attempting to set invalid values
rectangle.set_width(-2)         # Output: Invalid width value. Must be greater than 0.
rectangle.set_height(0)         # Output: Invalid height value. Must be greater than 0.
