tasks = []

def add_task(title, due_date, priority, tags):
    tasks.append({"title": title, "due_date": due_date, "priority": priority, "tags": set(tags)})

def complete_task(title):
    global tasks
    tasks = [t for t in tasks if t["title"] != title]