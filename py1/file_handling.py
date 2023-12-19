import json

# Reading from a File
# Opening a file in read mode
with open("example.txt", "r") as file:
    # Reading the entire file
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes leading and trailing whitespaces

# Writing to a File
# Opening a file in write mode
with open("output.txt", "w") as file:
    # Writing content to the file
    file.write("Hello, this is a sample file.\n")
    file.write("This is the second line.")

# Writing a dictionary to a JSON file
data = {"name": "John", "age": 30, "city": "New York"}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading JSON from a file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)

# Reading and Writing JSON (requires `import json` module)
# Writing a dictionary to a JSON file
data = {"name": "John", "age": 30, "city": "New York"}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading JSON from a file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)

# Exception Handling in File Operations
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print(content)
