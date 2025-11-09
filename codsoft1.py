# TO-DO LIST APPLICATION
tasks = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Multiple Tasks (Min 5, Max 10)")
    print("2. Mark Task (Done / Not Done)")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Exit")

# 1️ Add multiple tasks at once
def add_tasks():
    try:
        count = int(input("How many tasks do you want to add (5–10)? "))
        if count < 5 or count > 10:
            print(" Please enter a number between 5 and 10.")
            return

        for i in range(count):
            while True:
                title = input(f"Enter title for task {i+1}: ").strip()
                if title == "":
                    print("⚠️ Task title cannot be empty! Please enter something.")
                else:
                    task = {"title": title, "done": "No"}
                    tasks.append(task)
                    break  # Exit loop once valid input is entered

        print(f" {count} tasks added successfully!")

    except ValueError:
        print("Please enter a valid number!")

# 2️ Mark task as done or not done
def mark_task():
    if not tasks:
        print("No tasks available!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - Done: {task['done']}")
    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            status = input("Is the task done? (yes/no): ").strip().lower()
            if status == "yes":
                tasks[num - 1]['done'] = "Yes"
                print(f"Task '{tasks[num - 1]['title']}' marked as done ")
            elif status == "no":
                tasks[num - 1]['done'] = "No"
                print(f"Task '{tasks[num - 1]['title']}' marked as not done ")
            else:
                print("Invalid input! Please type yes or no.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# 3️ View all tasks
def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - Done: {task['done']}")

# 4️ Delete a task
def delete_task():
    if not tasks:
        print("No tasks to delete!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']}")
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed['title']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# 5️ Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1–5): ").strip()

    if choice == '1':
        add_tasks()
    elif choice == '2':
        mark_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List... Goodbye! ")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
