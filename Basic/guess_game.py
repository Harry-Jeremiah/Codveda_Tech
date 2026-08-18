"""
Task 2: Number Guessing Game
    Description: Write a program that randomly generates a number between 1 and 100. The user has to guess the number, and the program will give feedback if the guess is too high or too low

Objectives:
    Use the random module that generates a random number
    Give the user multiple attempts to guess the number
    Provide appropriate feedback("Too High" or "Too Low")
    Exit the game if the user guesses correctly or after a maximum number of attempts.

"""

print("===== GUESS GAME =====")
#using the random module
import random

#generating a random number between 1 and 100
number = random.randint(1, 100)

#creating number of attempts
attempts = 5

for attempt in range(attempts):
    try:

        choice = int(input("Guess the number: \n"))

        if choice == number:
            print("You have guessed right. Congratulations\n")
            break

        #when the number is too high
        elif choice > number:
            print("Your responsse is too high\n")

        #when the number is too low
        elif choice < number:
            print("Your response is too low\n")
    except ValueError:
        print("You have to enter a whole number")

    page.update()

else:
    print("You have used all your chances")
    print(f"The right number is {number} ")
