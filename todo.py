# Simple Todo App in Python
todo_list = []

def show_menu():
    print("\n--- TODO APP ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        task_number = int(input("Enter the task number to remove: "))
        if 0 < task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting Todo App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
