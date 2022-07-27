import random
from words import words
import string

def validWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = validWord(words)
    wordLetters = set(word)
    alphabet= set(string.ascii_uppercase)
    usedLetters= set() #what user has guessed 
    #getting input

    while len(wordLetters) > 0 :
        
        #letters used
        #''.join(['a','b' ,'c']) means string printed as 'a b c' 
        print('You have guessed: ', ' '.join(usedLetters))

        #tell current word with dash
        wordList=[letter if letter in usedLetters else '-' for letter in word]
        print('Current word: ', ' '.join(wordList))
        userInput= input('Guess a letter: ').upper()
        if userInput in alphabet not in usedLetters:
            usedLetters.add(userInput)
            if userInput in wordLetters:
                wordLetters.remove(userInput)

        elif userInput in userInput:
            print ('you have already guessed that letter')

        else: print ('Invalid Guess. try again')

print("congrats") #gets here when guessed all words

hangman()