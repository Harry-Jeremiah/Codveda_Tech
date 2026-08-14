"""
Task 1: To-Do List Application
    Description: Build a simple command-line to-do list application. Users should be able to read, delete, mark as done and list tasks.

Objectives:
    Implement the ability to add, view, and delete tasks
    Store the tasks in a file(either CSV or JSON format)
    Mark tasks as completed
    Implement basic error handling (trying to delete a task that doesn't exist)a

"""
import json


print("="*15,"TO-DO LIST", "="*15)
print()

tasks = []

#load tasks from json file
def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []

#save the tasks in json file
def save_task():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

#add tasks
def add_task():
    task = input("Enter the task you want to add: ")
    new_task = {
        "task": task,
        "Completed": False
    }

    tasks.append(new_task)

    save_task()

    print("Your task has been added to the list")

#view tasks
def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks in the list")
        return

    else:
        print("These are your tasks:")
        for number, task in enumerate(tasks, start=1):
            if task["Completed"]:
                status = "Complete"
            else:
                status = "Not complete"
            print(f"{number}. {task['task']} - {status}")
    print()   


#delete tasks
def delete_task():
    if len(tasks) == 0:
        print("There are no tasks in the list")
        return
    
    view_tasks()

    try:

        task_del = int(input("Enter the number of the task you want to delete: "))

        task_del = tasks.pop(task_del - 1)

        save_task()

        print("You have deleted ", task_del)

    except ValueError:
        print("Please enter a valid number")

    #error handling when deleting a task doesn't exist
    except IndexError:
        print("The task is not in your list.")

#mark as complete
def mark_complete():
    view_tasks()

    try:
        task_num = int(input("Enter the number of the task you want to mark as complete: "))

        task = tasks[task_num -  1]

        task["Completed"] = True

        save_task()

        print("Task is marked as complete.")

    except ValueError:
        print("Enter a valid number")
    except IndexError:
        print("The task is not in the list")

load_tasks()

print(tasks)

while True:

    print("You can perform the following tasks.\n")

    print("~"*30)
    print()
    print("1. Add tasks\n2. View tasks\n3. Delete tasks\n4. Mark as complete\n5. Exit\n")
    print("~"*30
      )

    try:
        choice = int(input("Enter your desired option: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_complete()
        elif choice == 5:
            print("These are your final tasks.")
            view_tasks()
            break
        else:
            print("Invalid choice, choose between 1 - 4")
    except ValueError:
        print("Please enter a number between 1 and 5")

