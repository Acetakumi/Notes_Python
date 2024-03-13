# Defining a simple function
def greet():
    print("Hello, World!")
greet()  # Calls the function and prints "Hello, World!"

# Passing parameters to a function
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Alice")  # Calls the function with "Alice" as the argument.

# Returning values from a function
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(result)  # Prints the sum of 5 and 3.

# Using default argument values
def greet_person_with_greeting(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet_person_with_greeting("Bob")  # Uses the default greeting "Hello".
greet_person_with_greeting("Bob", "Good morning")  # Uses "Good morning" as the greeting.

# Demonstrating different types of return values in Python functions

# Returning a Simple Variable
def compute_square(number):
    return number ** 2

# Returning a List
def get_fruits():
    return ["apple", "banana", "cherry"]

# Returning a Dictionary
def build_user(first_name, last_name):
    return {'first': first_name, 'last': last_name}

# Function that implicitly returns None (void functions)
def print_message(message):
    print(message)

# Let's call the functions and print their return values to demonstrate the different return types.
square_result = compute_square(4)
fruits_list = get_fruits()
user_dict = build_user('John', 'Doe')
none_result = print_message("Hello, World!")  # This will print the message and return None

# Printing results
square_result, fruits_list, user_dict, none_result

# Function accepting a list and returning a set (unique elements)
def list_to_set(lst):
    """Convert a list to a set of unique elements."""
    return set(lst)
