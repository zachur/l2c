class MyClass:
    def __init__(self):
        print("Object created.")

    def __del__(self):
        print("Object destroyed.")

# Creating an instance of the MyClass class
obj = MyClass()

# Explicitly deleting the object (calling the destructor)
del obj
