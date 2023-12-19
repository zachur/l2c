import numpy as np
from collections import deque

# Lists
my_list = [1, 2, 3, "apple", "banana"]

# Tuples
my_tuple = (1, 2, 3, "apple", "banana")

# Sets
my_set = {1, 2, 3, 4, 5}

# Dictionaries
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Strings
my_string = "Hello, World!"

# Arrays (using `numpy` library)
my_array = np.array([1, 2, 3, 4, 5])

# Stacks and Queues (using `deque` constructor of `collections` module)
my_stack = deque()
my_stack.append(1)
my_stack.append(2)
'''
print(my_stack.pop()) # Last-In, First-Out
print(my_stack.popleft()) # First-In, First-Out
'''
