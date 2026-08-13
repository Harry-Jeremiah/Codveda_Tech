"""
Task 1: Simple Calculator 
    Description: Develop a basic calculator that can perform the four primary arithmetic operations: addition, subtraction, multiplication and division.

Objectives:
    Create functions for each operation
    Take two inputs from the user and allow them to select the desired operation
    Handle the division by zero with appropriate error messages

"""

#creating functions for each operation
def add(number1, number2):
    sum = number1 + number2
    print(f"The sum is {sum}")

def subtract(number1, number2):
    difference = number1 - number2
    print(f"The difference is {difference}")

def divide(number1, number2):
    quotient = number1 / number2
    print(f"The quotient is {quotient}")

def multiply(number1, number2):
    product = number1 * number2
    print(f"The product is {product}")

#taking inputs from the user
try:

    figure1 = int(input("Enter your first number: "))
    figure2 = int(input("Enter your second number: "))

    print()

    #asking user to choose operation.
    print("You can do the follwing operations as below:" )
    print("1. Addition\n2. Subtraction\n3. Division\n4. Multiplication")

    choice = int(input("Enter a number from above to perform desired calculation: "))

    #performing desired operation
    if choice == 1:
        print("You have chosen addition")
        add(figure1, figure2)
    elif choice == 2:
        print("You have chosen subtraction")
        subtract(figure1, figure2)
    elif choice == 3:
        print("You have chosen division")
        divide(figure1, figure2)
    elif choice == 4:
        print("You have chosen multiplication")
        multiply(figure1, figure2)
    else:
        print("Invalid output")


except ValueError:
    print("You can only enter numbers")

#handling the division by zero error
except ZeroDivisionError:
    print("You cannot divide any nuumber by zero")
