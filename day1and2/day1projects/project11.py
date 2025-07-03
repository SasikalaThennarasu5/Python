# 11. To-Do List Manager
task1 = input("Enter task 1: ")
task2 = input("Enter task 2: ")
task3 = input("Enter task 3: ")
tasks = [task1, task2, task3]
print("\n📝 Your To-Do List:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")