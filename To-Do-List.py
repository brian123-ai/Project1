'''
PROBLEM STATEMENT:
Create a command-line interface (CLI) app that allows users to manage a to-do list.
Users should be able to add tasks, view tasks, mark tasks as completed, and delete tasks

'''

to_do_list = []
def show_tasks():
    if not to_do_list:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(to_do_list,1):
            print(f"{index}.{task}") 

def add_task(task):
    to_do_list.append(task)
    print('Task added successfully.')

def delete_task(task_number):
    if 0 < task_number <= len(to_do_list):
        removed_task = to_do_list.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted successfully.")
    else:
        print("Invalid task number.")

while True:
    print("\n === To-Do List === ")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        try:
            idx = int(input("Enter the task number to delete: "))
            delete_task(idx)
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == '4':
        print("Exiting the To-Do List app. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")   
