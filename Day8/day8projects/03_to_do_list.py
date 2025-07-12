# To-Do List Manager

tasks = ["Buy milk", "Call John", "Pay bills", "Finish homework"]

# Mark a task complete
tasks.remove("Call John")

# Show top priority tasks
print("Top tasks:", tasks[:2])

# Print with index
print("\nRemaining tasks:")
for i, task in enumerate(tasks):
    print(f"{i+1}. {task}")
