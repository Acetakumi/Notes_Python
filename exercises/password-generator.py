import random

def generate_random_password(length, listOfPossibleCharacters) -> str:
    password = ""
    for i in range(0,length,1): 
        x = random.randint(0,len(listOfPossibleCharacters)-1)
        password = password + listOfPossibleCharacters[x]
    return password
    
            
character_set = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+',
            '=', '{', '}', '[', ']', '|', ':', ';', '<', '>', ',', '.', '?', '/'
        ]

print(generate_random_password(16, character_set))