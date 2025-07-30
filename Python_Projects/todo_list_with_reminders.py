
import datetime
import time

# Decorator to time functions
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed {func.__name__} in {end - start:.4f} seconds")
        return result
    return wrapper

class Task:
    def __init__(self, name, deadline, status=False):
        self.name = name
        self.deadline = deadline  # (YYYY-MM-DD)
        self.status = status

    def __str__(self):
        due = "✅" if self.status else "❌"
        return f"{self.name} - Due: {self.deadline} - Status: {due}"

    def is_overdue(self):
        return not self.status and datetime.date.today() > datetime.date.fromisoformat(self.deadline)

    def is_due_today(self):
        return datetime.date.today() == datetime.date.fromisoformat(self.deadline)

class TaskManager:
    def __init__(self):
        self.tasks = []

    @timeit
    def add_task(self, name, deadline):
        try:
            datetime.date.fromisoformat(deadline)
            self.tasks.append(Task(name, deadline))
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    @timeit
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task} {'[OVERDUE]' if task.is_overdue() else ''}")

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task.name},{task.deadline},{task.status}\n")

    def load_from_file(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    name, deadline, status = line.strip().split(",")
                    self.tasks.append(Task(name, deadline, status == "True"))
        except FileNotFoundError:
            pass

    def __iter__(self):
        return (task for task in self.tasks if not task.status)

    def generate_due_today(self):
        return (task for task in self.tasks if task.is_due_today())

# Demo usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.load_from_file()

    while True:
        print("\n1. Add Task\n2. Complete Task\n3. Delete Task\n4. Show Tasks\n5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task name: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            manager.add_task(name, deadline)
        elif choice == "2":
            manager.show_tasks()
            index = int(input("Enter task number to complete: "))
            manager.complete_task(index)
        elif choice == "3":
            manager.show_tasks()
            index = int(input("Enter task number to delete: "))
            manager.delete_task(index)
        elif choice == "4":
            manager.show_tasks()
        elif choice == "5":
            manager.save_to_file()
            break
        else:
            print("Invalid choice.")
