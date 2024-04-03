# The `HangmanGame` class in Python implements a hangman game where players guess letters to reveal a
# secret word representing a country name.
#using oop

import random
import time 
import os
os.system('cls')  # Clear the terminal screen (Windows-specific)

class HangmanGame:
    HANGMAN_PICS = (
    r'''
    ┌───┐
    │   │
        │
        │
        │
        │
════════╛''', r'''
    ┌───┐
    │   │
    O   │
        │
        │
        │
════════╛''', r'''
    ┌───┐
    │   │
    O   │
    |   │
        │
        │
════════╛''', r'''
    ┌───┐
    │   │
    O   │
   /│   │
        │
        │
════════╛''', r'''
    ┌───┐
    │   │
    O   │
   /│\  │
        │
        │
════════╛''', r'''
    ┌───┐
    │   │
    O   │
   /│\  │
   /    │
        │
════════╛''', r'''
    ┌───┐
    │   │
    O   │
   /│\  │
   / \  │
        │
════════╛''')

    def __init__(self, countryList):
        """
        The `__init__` function initializes the attributes of the `HangmanGame` class.
        
        :param countryList: `countryList` is a list of countries
        """
        self.maxTrials = len(self.HANGMAN_PICS) - 1  # Maximum number of trials
        self.userInput = ""  # Letters guessed by the player
        self.trials = self.maxTrials  # Number of trials remaining
        self.randomCountry = random.choice(countryList).strip().upper()  # Country to guess
        self.secretWord = ""  # Current state of the secret word
        self.hint = self.calculateHintValue()  # Number of hints available
        self.iswin = 0  # Flag to track if the game is won

    def calculateHintValue(self):
        """
        The function calculates the hint value by dividing the length of the random country name by 2.
        :return: The length of the randomCountry attribute divided by 2.
        """
        return (len(self.randomCountry) // 2)-2

    def printDetails(self):
        """
        The function `printDetails` prints the hangman picture, the secret word, and a menu for the user
        to choose options.
        """
        os.system('cls')  # Clear the terminal screen
        print(player.HANGMAN_PICS[self.maxTrials - self.trials])
        print(f"""
Secret word :{self.secretWord}
MENU    
1.Enter the character
2.Use Hint .Hints remaining is {self.hint}
3.Show the answer
4.Exit""")

    def findSecretWord(self):
        """
        The function `findSecretWord` returns a string representation of the current progress of a
        hangman game.
        :return: The code is returning a string `s` that represents the current progress of the hangman
        game.
        """
        s = ""
        for i in self.randomCountry:
            if (i == " "):
                s += "   "
            elif (i in self.userInput):
                s += i + " "
            else:
                s += "_ "
        return s

    def findHint(self):
        """
        The function "findHint" decreases the hint count by 1, selects a letter from random country that has not
        been entered by the user, and returns it as a hint.
        :return: a randomly chosen country name from the list `self.randomCountry`, as long as it is not
        already in `self.userInput` and is not an empty string. If there are no more hints available
        (`self.hint` is 0), it prints "No More Hint Try Again" and returns an empty string.
        """
        if self.hint > 0:
            self.hint -= 1
            while True:
                rand = random.choice(self.randomCountry)
                if rand not in self.userInput and rand != " ":
                    return rand
        else:
            return ""

    def win(self):
        """
        The function checks if all the characters in the randomCountry string are present in the
        userInput string, and returns 1 if they are, otherwise it returns 0.
        :return: either 1 or 0. If all the characters in the randomCountry string are present in the
        userInput string, except for spaces, then the function returns 1. Otherwise, it returns 0.
        """
        f = 1
        for i in self.randomCountry:
            if i not in self.userInput and i != " ":
                f = 0
                break
        if f == 1:
            self.iswin = 1
            return 1
        else:
            return 0

    def play(self):
        """
        The function `play` is a game loop that allows the user to guess letters, get hints, reveal the
        answer, or exit the game, and it keeps track of the user's progress and number of trials.
        """
        self.userInput+=self.randomCountry[0]
        self.secretWord = self.findSecretWord()
        self.printDetails()
        while(self.trials > 0):
            if(self.win() == 1):
                print("YOU WIN ")
                break
            try:
                choice = int(input("Enter your choice "))
            except:
                print("Enter Integer")
                time.sleep(0.8)
                continue
            print(f"Choice is {choice}")
            if choice == 1:
                userinput = input("Enter the character ").upper()
                if userinput.isdigit() or (userinput.isalpha() and len(userinput) > 1):
                    print('The Input is not a letter ')
                    continue
                elif userinput in self.userInput:
                    print("You Already Guessed That Letter ")
                elif userinput in self.randomCountry:
                    self.userInput += userinput
                    print("Correct")
                else:
                    print("WRONG")
                    self.trials -= 1
                time.sleep(1)
            elif choice == 2:
                rand = self.findHint()
                try:
                    print(f"hint: {rand} ascii is {ord(rand)}")
                except:
                    print("NO MORE HINT")
                time.sleep(1)
                self.userInput += rand
            elif choice == 3:
                print(f"Answer is {self.randomCountry}")
                time.sleep(1)
                break
            elif choice == 4:
                exit()
            else:
                print("Wrong Choice. Try Again")
                time.sleep(0.80)
            
            self.secretWord = self.findSecretWord()
            self.printDetails()

        if self.iswin == 0:
            print("YOU LOSE")

if __name__ == "__main__":
    f = open(r"D:\RIDHIN\COmputer\Python\name the country\capital.txt", "r")
    countries = f.readlines()
    player = HangmanGame(countries)
    player.play()
