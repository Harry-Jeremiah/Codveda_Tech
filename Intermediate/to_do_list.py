"""
Task 1: To-Do List Application
    Description: Build a simple command-line to-do list application. Users should be able to read, delete, mark as done and list tasks.

Objectives:
    Implement the ability to add, view, and delete tasks
    Store the tasks in a file(either CSV or JSON format)
    Mark tasks as completed
    Implement basic error handling (trying to delete a task that doesn't exist)a

"""

print("===== TO-DO LIST =====")
print()

tasks = []

#add tasks
def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)

    print("Your task has been added to the list")

#view tasks
def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks in the list")

    else:
        print("These are your tasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

#delete tasks
def delete_task():
    try:

        task_del = int(input("Enter the number of the task you want to delete: "))

        task_del = tasks.pop(task_del - 1)

        print("You have deleted ", task_del)

    except ValueError:
        print("Please enter a valid number")

    #error handling when deleting a task doesn't exist
    except IndexError:
        print("The task is not in your list.")

print("You can perform the following tasks.\n")

print("~"*25)
print()
print("1. Add taks\n2. View tasks\n3. Delete tasks\n4. Exit\n")
print("~"*25)

choice = int(input("Enter your desired option: "))

if choice == 1:
    add_task()
elif choice == 2:
    view_tasks()
elif choice == 3:
    delete_task()
elif choice == 4:
    print("Thank you. Goodbye")
else:
    print("Invalid choice, choose between 1 - 4")

