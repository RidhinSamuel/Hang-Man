"""
The Python script is a guessing game where the player needs to guess a random country name by
entering characters, getting hints, or guessing the full answer.
"""
import random 
import time
import os
os.system('cls')
def printBlank():
    """
    The function `printBlank` clears the console, prints a message, and then prints a series of
    underscores and spaces based on the characters in a random country name.
    """
    os.system('cls')
    print("Guess the country")
    for i in randomCountry:
        if (i==" "):
            print(" ",end="  ")
        elif (i in gameProgress):
            print(i,end=" ")
        else:
            print("_ ",end="")

def inputCharacter(ch):
    """
    The function `inputCharacter` checks if a given character is in a list called `randomCountry`, and if
    it is, it adds the character to a variable called `gameProgress`.
    :param ch: The parameter `ch` is a character that is being passed to the `inputCharacter` function
    """
    global gameProgress
    if(ch in randomCountry):
        print("True")
        gameProgress=gameProgress+ch
        time.sleep(2)
    else:
        print("Wrong Guess ")
        time.sleep(1)

def findHint():
    """
    The function `findHint` is used to provide a hint to the user during a guessing game, by selecting a
    random country that has not been guessed yet.
    """
    global hint
    if (hint<1):
        print("No More Hint Try Again")
        time.sleep(1)
    else:
        hint=hint-1
        while(True):
            rand=random.choice(randomCountry)
            if(rand not in gameProgress):
                inputCharacter(rand)
                break
    


f=open(r"D:\RIDHIN\COmputer\Python\name the country\country.txt","r")
hint=3
content=f.readlines()
randomCountry=random.choice(content)
gameProgress=""
randomCountry=randomCountry.upper().rstrip()
if(len(randomCountry)<=4):
    hint=1
elif(len(randomCountry)<7):
    hint=2
elif(len(randomCountry)>10):
    hint=4
option=-1
gameProgress+=randomCountry[0]
#Find_Hint()
while(True):
    printBlank()
    f=1
    for i in randomCountry:
            if i not in gameProgress and i!=" ":
                f=0
                break
    if f==1:
        print(f"\nYou Guessed Correct :-{randomCountry}")
        break
    #print(random_country)
    option=int(input(f"""
MENU 
1.Enter the Character
2.Hint {hint}
3.Enter the Answer
4.Show The Answer
5.Exit
"""))
    if(option==1):
        ch=input("\nEnter the character ")
        inputCharacter(ch.upper())
        f=1
        """This code is checking if there are any characters in the `random_country` string that have
         not been guessed yet (`i not in user`) and are not spaces (`i!=" "`). If such a character is
         found, it sets `f` to 0 and breaks out of the loop. This is used to determine if all the
         characters in the country name have been guessed correctly."""
        for i in randomCountry:
            if i not in gameProgress and i!=" ":
                f=0
                break
        if f==1:
            printBlank()
            print(f"\nYou Guessed Correct :-{randomCountry}")
            break
    elif(option==2):
        findHint()
    elif(option==4):
        printBlank()
        print(f"\nAnswer is {randomCountry}")
        break
    elif(option==5):
        exit()
    elif(option==3):
        printBlank()
        answer=input("\nEnter the country name")
        if (answer.upper().rstrip()==randomCountry):
            print(f"\nYou Guessed Correct :-{randomCountry}")
            time.sleep(1)
            break
        else:
            print("Wrong guess")
            time.sleep(1)
    else:
        print("Wrong Choice Try Again")
        time.sleep(1)
        print("\r")
        




