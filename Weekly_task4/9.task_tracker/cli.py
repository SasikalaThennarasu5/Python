from task_ops import *

add_task("Finish report", "2025-07-22", "High", ["work"])
add_task("Buy groceries", "2025-07-20", "Low", ["home"])

for t in tasks:
    print(t)