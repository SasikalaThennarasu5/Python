import time
from datetime import datetime, date
from functools import wraps

# ------------------ Decorator to Time Functions ------------------ #
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.4f} seconds")
        return result
    return wrapper

# ------------------ Task Class ------------------ #
class Task:
    def __init__(self, name, deadline, status="Pending"):
        self.name = name
        try:
            self.deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Deadline must be in YYYY-MM-DD format")
        self.status = status

    def __str__(self):
        overdue = self.deadline < date.today() and self.status == "Pending"
        flag = " (OVERDUE!)" if overdue else ""
        return f"{self.name:20} | Due: {self.deadline} | Status: {self.status}{flag}"

# ------------------ To-Do Manager ------------------ #
class ToDoList:
    def __init__(self):
        self.tasks = []

    @timeit
    def add_task(self, name, deadline):
        try:
            task = Task(name, deadline)
            self.tasks.append(task)
            print("Task added.")
        except ValueError as e:
            print(e)

    @timeit
    def complete_task(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                task.status = "Completed"
                print("Task marked as completed.")
                return
        print("Task not found.")

    @timeit
    def delete_task(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                self.tasks.remove(task)
                print("Task deleted.")
                return
        print("Task not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- To-Do List ---")
        for task in self.tasks:
            print(task)

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task.name}|{task.deadline}|{task.status}\n")
        print("Tasks saved to file.")

    def load_from_file(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    name, deadline, status = line.strip().split("|")
                    self.tasks.append(Task(name, deadline, status))
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No saved tasks found.")

    def __iter__(self):
        return (task for task in self.tasks if task.status == "Pending")

    def tasks_due_today(self):
        today = date.today()
        return (task for task in self.tasks if task.deadline == today and task.status == "Pending")

# ------------------ Menu Interface ------------------ #
def main():
    todo = ToDoList()
    todo.load_from_file()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. View Pending Tasks")
        print("6. View Today's Tasks")
        print("7. Save Tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Task Name: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            todo.add_task(name, deadline)

        elif choice == "2":
            name = input("Enter task name to complete: ")
            todo.complete_task(name)

        elif choice == "3":
            name = input("Enter task name to delete: ")
            todo.delete_task(name)

        elif choice == "4":
            todo.display_tasks()

        elif choice == "5":
            print("\n--- Pending Tasks ---")
            for task in todo:
                print(task)

        elif choice == "6":
            print("\n--- Tasks Due Today ---")
            for task in todo.tasks_due_today():
                print(task)

        elif choice == "7":
            todo.save_to_file()

        elif choice == "8":
            todo.save_to_file()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
