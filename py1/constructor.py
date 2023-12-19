class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} created.")

# Creating an instance of the Person class (calling the constructor)
person = Person("Alice", 30)

# Accessing attributes
print(f"{person.name} is {person.age} years old.")
