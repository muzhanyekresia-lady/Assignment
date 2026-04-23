{ " task": "buy home_supplies", "done": True}
import json
import os

FILE_NAME = "tasks.json"


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- Your Tasks ---")
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. {t['task']} [{status}]")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")


def mark_completed(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except:
                return []
    return []


# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved.")
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()