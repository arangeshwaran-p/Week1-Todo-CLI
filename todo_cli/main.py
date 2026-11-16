"""Command line interface for the To-Do List Manager."""

from todo_cli.task_manager import TaskManager
from todo_cli.storage import load_tasks, save_tasks

def show_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("\nYour task list is empty.")
        return

    print("\n--- YOUR TASKS ---")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} [{status}]')

def get_task_id():
    try:
        task_id = int(input("Enter task ID: "))
        if task_id <= 0:
            print("Please enter a positive task ID.")
            return None
        return task_id
    except ValueError:
        print("Invalid input. Enter the task ID as a number.")
        return None

def main():
    manager = TaskManager()
    load_tasks(manager)

    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task description: ")
            try:
                manager.add_task(title)
                save_tasks(manager)
                print("Task added successfully.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            show_tasks(manager)

        elif choice == "3":
            show_tasks(manager)
            task_id = get_task_id()
            if task_id is not None:
                try:
                    manager.complete_task(task_id)
                    save_tasks(manager)
                    print("Task marked as completed.")
                except ValueError as error:
                    print(error)

        elif choice == "4":
            show_tasks(manager)
            task_id = get_task_id()
            if task_id is not None:
                try:
                    manager.remove_task(task_id)
                    save_tasks(manager)
                    print("Task removed successfully.")
                except ValueError as error:
                    print(error)

        elif choice == "5":
            print("Thank you for using the To-Do List Manager!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
