listOfMyNotes = []
for i in range(0,4,1):
   Notes = int(input("what is your graden : ")) 
   listOfMyNotes.append(Notes)
   
moyenne = 0
for i in range(0,len(listOfMyNotes),1):
    moyenne = listOfMyNotes[i] + moyenne

print(moyenne/len(listOfMyNotes))
