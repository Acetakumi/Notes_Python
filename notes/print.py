# Basic print usage: prints the string as is.
print("Hello, World!")

# Printing multiple items separated by spaces by default.
print("Hello,", "World!")

# Using the 'sep' parameter to change the separator.
print("Hello,", "World!", sep="-")  # Output: Hello,-World!

# Using the 'end' parameter to change the ending character (default is newline).
print("Hello,", end=" ")
print("World!")  # Output: Hello, World!

# Printing on the same line using the 'end' parameter.
print("Hello,", end="")
print("World!")  # Output: HelloWorld!

# Printing with formatting using f-strings (formatted string literals).
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.

# Printing special characters like newline (\n) and tab (\t).
print("Line 1\nLine 2\nLine 3")  # Outputs three lines.
print("Column 1\tColumn 2\tColumn 3")  # Outputs text with tab spaces between words.