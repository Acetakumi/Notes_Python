
import random


listOfRandomNumbers = list(range(200))

randomnumber = random.randint(0,len(listOfRandomNumbers)-1)
 
for i in range(0,len(listOfRandomNumbers),1) : 
    usersguess = input("what is ur guess : ")
    usersguess = int(usersguess)
    if usersguess < randomnumber :
        print("too low")
    elif usersguess > randomnumber : 
        print("too high")
    elif usersguess == randomnumber :
        print("that is correct answer")
        break

print("thanks fro playing")
        