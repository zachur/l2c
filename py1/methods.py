# Method Definition
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says woof!")

my_dog = Dog("Buddy")

# Method Invocation
my_dog.bark()

# Instance Methods versus Class Methods
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        print("Instance method:", self.instance_variable)

    @classmethod
    def class_method(cls):
        print("Class method:", cls.class_variable)

obj = MyClass("I am an instance variable")
obj.instance_method()
MyClass.class_method()