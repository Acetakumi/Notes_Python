def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

print("\n\n1 - Addition")
print("2 - Substraction")
print("3 - Multiplication")
print("4 - Division")
print("0 - Exit\n")

choice = input("--> ")

while choice != "0":
    num1 = float(input("Choose a number: "))
    num2 = float(input("Choose a number: "))
    
    if choice == "1":
        print(addition(num1, num2))
    
    if choice == "2":
        print(substraction(num1, num2))
        
    if choice == "3":
        print(multiply(num1, num2))
        
    if choice == "4":
        print(divide(num1, num2))
        
    print("\n\n1 - Addition")
    print("2 - Substraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("0 - Exit\n")

    choice = input("--> ")