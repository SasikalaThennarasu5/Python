tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({'task': task, 'done': False})

def delete_task():
    show_tasks()
    try:
        idx = int(input("Task number to delete: ")) - 1
        tasks.pop(idx)
    except:
        print("Invalid.")

def mark_complete():
    show_tasks()
    try:
        idx = int(input("Task number to mark complete: ")) - 1
        tasks[idx]['done'] = True
    except:
        print("Invalid.")

def show_tasks():
    for i, t in enumerate(tasks):
        status = "✓" if t['done'] else "✗"
        print(f"{i+1}. {t['task']} [{status}]")

while True:
    print("\n1. Add\n2. Delete\n3. Mark Complete\n4. Show All\n5. Exit")
    ch = input("Choose: ")
    if ch == '1': add_task()
    elif ch == '2': delete_task()
    elif ch == '3': mark_complete()
    elif ch == '4': show_tasks()
    elif ch == '5': break
    else: print("Invalid.")
