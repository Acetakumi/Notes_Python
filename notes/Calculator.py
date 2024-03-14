options = int(input("choose one of the following option,\n 1-Addition,\n 2-Soustraction, \n 3-Multiplication, \n 4-Division, \n 0 -quit the application \n chosse a option : "))

def addition (number1,number2):
    final = number1 + number2 
    return final
    
def soustraction (number1,number2) : 
    final = number1 - number2
    return final
    
def multiplication (number1,number2):
    final = number1 *number2 
    return final
    
def Division (number1,number2):
    final = number1/number2
    return final
    
while True : 
    if options == 1 :
        x = int(input("what is ur first number : "))
        y = int(input("what is ur second number : "))
        print(addition(x,y))
        options = int(input("choose one of the following option,\n 1-Addition,\n 2-Soustraction, \n 3-Multiplication, \n 4-Division, \n 0 -quit the application \n chosse a option : "))
    elif options == 2 : 
        x = int(input("what is ur first number : "))
        y = int(input("what is ur second number : "))
        print(soustraction(x,y))
        options = int(input("choose one of the following option,\n 1-Addition,\n 2-Soustraction, \n 3-Multiplication, \n 4-Division, \n 0 -quit the application \n chosse a option : "))
    elif options == 3 : 
        x = int(input("what is ur first number : "))
        y = int(input("what is ur second number : "))
        print(multiplication(x,y))
        options = int(input("choose one of the following option,\n 1-Addition,\n 2-Soustraction, \n 3-Multiplication, \n 4-Division, \n 0 -quit the application \n chosse a option : "))
    elif options == 4 :
        x = int(input("what is ur first number : "))
        y = int(input("what is ur second number : "))
        print(Division(x,y))
        options = int(input("choose one of the following option,\n 1-Addition,\n 2-Soustraction, \n 3-Multiplication, \n 4-Division, \n 0 -quit the application \n chosse a option : "))
    else : 
        break
        
        