# To-Do List in Python

tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save Tasks to File")
    print("5. Load Tasks from File")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved to tasks.txt")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            loaded = f.readlines()
            global tasks
            tasks = [task.strip() for task in loaded]
            print("Tasks loaded from file.")
    except FileNotFoundError:
        print("No saved tasks found.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        save_tasks()
    elif choice == '5':
        load_tasks()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
