class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    # Overriding the make_sound method
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    # Overriding the make_sound method
    def make_sound(self):
        return "Meow!"

# Creating instances of the subclasses
dog = Dog()
cat = Cat()

# Calling the overridden method
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
