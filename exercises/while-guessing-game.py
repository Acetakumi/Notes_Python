import random

randomNumber = random.randint(0, 50)

userInput = int(input("What is your guess: "))
while userInput != randomNumber:
    if userInput > randomNumber :
        print ("too high")
    else :
        print("too low")
    userInput = int(input("What is your guess: "))
    
print("you have the correct answer")  

       
        
