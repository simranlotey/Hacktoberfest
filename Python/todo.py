# Initialize an empty to-do list
todo_list = {}

def add_task(task, priority):
    todo_list[task] = priority
    print(f"Task '{task}' added with priority {priority}.")

def view_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for task, priority in sorted(todo_list.items(), key=lambda x: x[1]):
            print(f"Task: {task}, Priority: {priority}")

def remove_task(task):
    if task in todo_list:
        del todo_list[task]
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task: ")
            priority = input("Enter the priority (high/medium/low): ")
            add_task(task, priority)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Simple To-Do List Manager")
    main()