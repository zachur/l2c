# Try-Except Blocks
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Cannot divide by zero.")
except Exception as e:
    # Code to handle other exceptions
    print(f"An error occurred: {e}")
else:
    # Code to execute if no exception is raised
    print("Division successful.")
finally:
    # Code that will be executed no matter what
    print("This will always be executed.")

# Handling Multiple Exceptions
try:
    # Code that might raise an exception
    num = int("abc")
except (ValueError, TypeError) as e:
    # Code to handle multiple exceptions
    print(f"Conversion error: {e}")

# Raising Exceptions
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # Raise a custom exception
        raise ValueError("Cannot divide by zero.")
    else:
        return result

try:
    print(divide(10, 0))
except ValueError as ve:
    print(f"Error: {ve}")

# Using `finally` for Cleanup
try:
    file = open("example.txt", "r")
    # Code that might raise an exception
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    # Close the file in the finally block to ensure it's always closed
    file.close()


