# To-Do List Manager

import json
from datetime import datetime

class Task:
    def __init__(self, title, priority=3, due_date=None, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            'title': self.title,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data['title'], data['priority'], data['due_date'], data['completed'])

class ToDoList:
    def __init__(self, file_path='tasks.json'):
        self.tasks = []
        self.file_path = file_path
        self.load_tasks()

    def add_task(self, title, priority=3, due_date=None):
        self.tasks.append(Task(title, priority, due_date))

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True

    def view_tasks(self):
        return sorted(self.tasks, key=lambda x: (x.priority, x.due_date or '9999'))

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower()]

    def save_tasks(self):
        with open(self.file_path, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            self.tasks = []

# CLI for demo
if __name__ == "__main__":
    todo = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task\n2. Delete Task\n3. View Tasks\n4. Mark Complete\n5. Search\n6. Save & Exit")
        choice = input("Choose: ")
        if choice == '1':
            title = input("Task title: ")
            priority = int(input("Priority (1=High, 5=Low): "))
            due_date = input("Due Date (YYYY-MM-DD) [optional]: ") or None
            todo.add_task(title, priority, due_date)
        elif choice == '2':
            title = input("Task title to delete: ")
            todo.delete_task(title)
        elif choice == '3':
            for task in todo.view_tasks():
                print(f"{'[x]' if task.completed else '[ ]'} {task.title} - Priority {task.priority} - Due: {task.due_date}")
        elif choice == '4':
            title = input("Task title to mark complete: ")
            todo.mark_complete(title)
        elif choice == '5':
            keyword = input("Search keyword: ")
            results = todo.search_tasks(keyword)
            for task in results:
                print(f"{task.title} - Priority {task.priority}")
        elif choice == '6':
            todo.save_tasks()
            print("Tasks saved. Exiting.")
            break
