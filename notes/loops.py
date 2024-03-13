# FOR LOOP
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.

# Iterating over a list.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Prints each fruit in the fruits list.

# The range() function has a start, stop, and step values: range(start, stop, step).
for number in range(2, 10, 2):  # Will print even numbers between 2 and 8.
    print(number)

# WHILE LOOP
# The while loop in Python is used to execute a block of statements as long as a condition is true.

count = 0
while count < 5:
    print(count)  # Prints count as long as it is less than 5.
    count += 1  # Increment count by 1.

# BREAK
# The break statement is used to exit the loop when a certain condition is met.

for number in range(10):
    if number == 5:
        break  # Exits the loop when number is 5.
    print(number)  # Prints numbers 0 to 4.

# Nested loops: A loop inside another loop.
for i in range(2):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"i: {i}, j: {j}")  # Prints combination of i and j values.