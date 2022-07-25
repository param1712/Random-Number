from random import random


def guess(x):
    randomNumber= random.randint(1,x)
    guess =0
    while guess != randomNumber:
        guess= int(input(f'Guess a number between 1 and {x}:'))
        if guess <randomNumber:
            print("Sorry.Too low")
        elif guess >randomNumber:
            print("sorry.Too high")

    print(f'Congratulations You have guessed the rigth number {randomNumber}')
guess=10