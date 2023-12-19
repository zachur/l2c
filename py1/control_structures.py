'''
Conditional Statements
'''

# If, Elif, Else
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

'''
Loops
'''

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

'''
Control Statements
'''

# Break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

'''
Conditional Expressions
'''

# Ternary Operator
age = 20
can_vote = "Yes" if age >= 18 else "No"
print("Can vote?", can_vote)

'''
Exception Handling
'''

# Try, Except, Finally
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("This will always be executed")

'''
Switch Statements
'''

def case_one():
    return "This is case one"

def case_two():
    return "This is case two"

def case_default():
    return "This is the default case"

switch = {
    1: case_one,
    2: case_two,
}

result = switch.get(3, case_default)()
print(result)
