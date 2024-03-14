
import os
from passwordGenerator import generate_random_password

key = {'!': 'Y',
                    '"': 'm',
                    '#': 'u',
                    '$': ':',
                    '%': '@',
                    '&': 'p',
                    "'": '1',
                    '(': 'X',
                    ')': '+',
                    '*': '}',
                    '+': ',',
                    ',': 'K',
                    '-': '$',
                    '.': 'B',
                    '/': '5',
                    '0': 'I',
                    '1': 'Z',
                    '2': 'A',
                    '3': 'h',
                    '4': 'O',
                    '5': '=',
                    '6': 'U',
                    '7': 'T',
                    '8': '*',
                    '9': 'g',
                    ':': 's',
                    ';': 'D',
                    '<': '0',
                    '=': '!',
                    '>': '>',
                    '?': ';',
                    '@': 'd',
                    'A': '8',
                    'B': '7',
                    'C': '(',
                    'D': 'i',
                    'E': '-',
                    'F': 'z',
                    'G': "op",
                    'H': '%',
                    'I': '~',
                    'J': 'H',
                    'K': 'x',
                    'L': 'S',
                    'M': 'n',
                    'N': '[',
                    'O': 't',
                    'P': '2',
                    'Q': '<',
                    'R': '3',
                    'S': 'J',
                    'T': 'q',
                    'U': 'y',
                    'V': '6',
                    'W': 'f',
                    'X': 'o',
                    'Y': 'b',
                    'Z': '^',
                    '[': '_',
                    '\\': '?',
                    ']': 'w',
                    '^': '"',
                    '_': '4',
                    '`': 'Q',
                    'a': 'M',
                    'b': '{',
                    'c': 'j',
                    'd': ')',
                    'e': '&',
                    'f': 'a',
                    'g': '#',
                    'h': '/',
                    'i': 'F',
                    'j': 'V',
                    'k': 'v',
                    'l': "'",
                    'm': 'e',
                    'n': 'c',
                    'o': ']',
                    'p': 'k',
                    'q': 'E',
                    'r': 'N',
                    's': 'L',
                    't': 'C',
                    'u': '`',
                    'v': 'W',
                    'w': 'G',
                    'x': '.',
                    'y': 'r',
                    'z': 'R',
                    '{': '9',
                    '|': '\\',
                    '}': 'P',
                    '~': 'l'}


mode = input("\n1-Add a username and password \n2-View a username and password \n3-quit the function \n4-Decrypt the password \n5-Delete current password repository \nwhich option do you want : ")

def encrypt (plainTextPwd) : 
    encyptedempty = ""
    for i in range (0,len(plainTextPwd),1) : 
        encyptedempty = encyptedempty + key[plainTextPwd[i]]
    
    return encyptedempty

def getKeyFromValue(d, value):
    keys = [str(key) for key, val in d.items() if val == value]
    return ', '.join(keys)

def decrypt(encryptedTextPwd) :
    decryptedempty = "" 
    for i in range(0,len(encryptedTextPwd)) :
            decryptedempty = decryptedempty +  getKeyFromValue(key,encryptedTextPwd[i])
    
    return decryptedempty







def view (): 
    with open("./exercises/Data/password.txt","r") as file : 
        alltext = file.readlines()
        os.system("cls")
        for line in range(0,len(alltext),1) :
            split = alltext[line].replace("\n","")
            currentLine = split.split("|")
            user = currentLine[0]
            password = currentLine[1]
            print( "------------------------------------------" + "\n" + "usernamme : " + user + "\n" + "password : " + password)
    
        x = input("\n\nEnter to continue \n\n")
        os.system("cls")



def add() : 
    username = input("\nAdd a username : ")
    x = input("\nDo you wish to have a randomly generated password (yes or no) : ")
    if x == "yes" :
        password = int(input("\nHow many characters do you wish to have : "))
        generate_random_password(password)
        randomPassword = generate_random_password(password)
        with open("./exercises/Data/password.txt","a") as file :
            file.write(username + "|" + encrypt(randomPassword) + "\n")
            print(encrypt(randomPassword))


    else : 
        password = input("\nAdd a password : ")
        with open("./exercises/Data/password.txt","a") as file :
            file.write(username + "|" + encrypt(password) + "\n")





        


while True :
    if mode == "3":
        break 
    if mode == "4" : 
        x = input("\nwhat is the password to access to the decryption  : ")
        if x == "Ace" : 
            print("\nAccess Granted")
            y = input("\nwhat do you wish to have decrypted : ")
            print("\n" + decrypt(y))
        else : 
            os.system("cls")
            print("\nAcess Denied")
            break
    elif mode == "1" :
        add()
    elif mode == "2":
        view()
    elif mode == "5":
        x = input("\nWhat is the password to exterminate this file : ")
        if x == "Hasilon" :
            print("\nAcess Granted \n\nFiles have been terminate")
            with open("./exercises/Data/password.txt","w") as file :
                file.write("")
        else : 
            os.system("cls")
            print("\nAcess Denied")
            break
    else : 
        print("invalid")
    mode = input("\n1-Add a username and password \n2-View a username and password \n3-quit the function \n4-Decrypt the password \n5-Delete current password repository \nwhich option do you want : ")

        