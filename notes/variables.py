# Integer: Whole numbers without a fraction.
integer_variable = 10
print(integer_variable)  # Output: 10

# Float: Numbers with a decimal point.
float_variable = 10.5
print(float_variable)  # Output: 10.5

# String: Text or characters surrounded by quotes.
string_variable = "Hello, World!"
print(string_variable)  # Output: Hello, World!

# Boolean: Represents True or False.
boolean_variable = True  # Can be True or False
print(boolean_variable)  # Output: True

# List: An ordered collection of items. Lists are mutable (can be changed).
list_variable = ["apple", "banana", "cherry"]
print(list_variable)  # Output: ['apple', 'banana', 'cherry']

# Accessing list items by index. Indexing starts at 0.
print(list_variable[0])  # Output: apple
print(list_variable[1])  # Output: banana

# Negative indexing starts from the end. -1 is the last item, -2 is the second last, and so on.
print(list_variable[-1])  # Output: cherry

# Slicing lists to get sublists. Syntax: list[start:stop:step]
print(list_variable[0:2])  # Output: ['apple', 'banana'] (includes index 0, excludes index 2)

# Dictionary: A collection of key-value pairs. Dictionaries are mutable.
dictionary_variable = {"name": "Alice", "age": 30}
print(dictionary_variable)  # Output: {'name': 'Alice', 'age': 30}

# Accessing dictionary items using keys.
print(dictionary_variable["name"])  # Output: Alice
print(dictionary_variable["age"])  # Output: 30

# Adding or updating dictionary items.
dictionary_variable["location"] = "New York"
print(dictionary_variable)  # Output includes 'location': 'New York'

# Using get() to access dictionary items. Returns None if key does not exist, avoiding KeyError.
print(dictionary_variable.get("name"))  # Output: Alice
print(dictionary_variable.get("nonexistent_key"))  # Output: None

# Tuple: An ordered collection of items. Tuples are immutable (cannot be changed).
tuple_variable = ("apple", "banana", "cherry")
print(tuple_variable)  # Output: ('apple', 'banana', 'cherry')

# Accessing tuple items by index.
print(tuple_variable[0])  # Output: apple

# Set: An unordered collection of unique items (removes duplicates). Sets are mutable (can be changed).
set_variable = {"apple", "banana", "cherry"}
print(set_variable)  # Note: Sets do not support indexing or ordering.

# Adding items to a set.
set_variable.add("orange")
print(set_variable)

# Removing items from a set.
set_variable.remove("banana")
print(set_variable)