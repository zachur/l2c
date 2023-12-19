# Base class (parent class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # Abstract method, to be overridden by subclasses

    def display_info(self):
        print(f"{self.name} - {self.species}")

# Derived class (subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the constructor of the base class
        super().__init__(name, species="Dog")
        self.breed = breed

    # Overriding the make_sound method
    def make_sound(self):
        return "Woof!"

# Another derived class (subclass)
class Cat(Animal):
    def __init__(self, name, color):
        # Calling the constructor of the base class
        super().__init__(name, species="Cat")
        self.color = color

    # Overriding the make_sound method
    def make_sound(self):
        return "Meow!"

# Creating instances of the derived classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")

# Using inherited methods
dog.display_info()
print(dog.make_sound())

cat.display_info()
print(cat.make_sound())
