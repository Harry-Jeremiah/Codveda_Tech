"""
Task 3: Word Counter
    Description: Create a python program that reads a text file and counts the number of words in it.

Objectives
    Read the content of a file 
    Split the content into words and counts them
    Handle exceptions such as file not found

"""

try:
    #read the content
    with open("tasks.txt", "r") as file:
        content = file.read()

        #splitting the words 
        words = content.split()
        print(f"The file contains {len(words)} words")

except FileNotFoundError:
    print("The filename does not exist.")
    