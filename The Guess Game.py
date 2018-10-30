"""
Created on Mon-May 14 23:04:14 2018

@author: Ben Yeamin
"""

from random import randint
print("\n\n                          ***Welcome to Guess Game***\n                           ========================\n")

game = input("Wanna play a game? yes or no? Type Y/N > ")
print("\n")

print("I'm thinking a number between 1-50...\n Guess what is it.... \n\n")
if game == "N":
    print("Okay bye bye!!")
elif game == "Y":
    secret_num = randint(1,50)
    num_guess = 0
    guess = 0

    while guess != secret_num and num_guess <= 4:
        guess = eval(input("Enter your guess between 1,50: "))
        num_guess = num_guess + 1
        if guess < secret_num:
            print("Guess HIGHER next time...\n" , "Man..! you have ",5-num_guess , "guesses left\n")
        elif guess > secret_num:
            print("Guess LOWER next time...\n", "Man..! you have ",5-num_guess , "guesses left\n")
        else:
            print("Wow..! You got it...\n")

    if num_guess == 5 and guess != secret_num:
        print("You lose! The correct number is: " , secret_num , "\n")


input("Enter any key to close")
