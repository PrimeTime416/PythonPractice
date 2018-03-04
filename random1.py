#!/user/bin/env python3


# Atalyah's program


import random


def main():
    print("Guess a number between 1 and 10")
    randomNumber = random.randint(1, 10)
    # print(randomNumber)
    while True:
        userGuess = int(input("your Guess: "))
        # userGuess = input("your Guess: ")
        print(userGuess)
        # print(randomNumber)
        # print(userGuess == randomNumber)
        # print(10 == 10.0)
        if userGuess == randomNumber:
            print("you are correct")


main()
