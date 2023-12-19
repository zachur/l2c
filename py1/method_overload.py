class Calculator:
    def add(self, a, b=0):
        return a + b

# Creating an instance of the Calculator class
calculator = Calculator()

# Overloaded method with one or two arguments
result1 = calculator.add(5)
result2 = calculator.add(3, 7)

print(f"Result 1: {result1}")  # Output: Result 1: 5
print(f"Result 2: {result2}")  # Output: Result 2: 10
