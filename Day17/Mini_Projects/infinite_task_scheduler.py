
import time
import itertools
from datetime import datetime

# Step 1: Define background tasks
tasks = [
    "Sync Files",
    "Backup Database",
    "Send Email Notifications",
    "Clear Cache",
    "Generate Reports"
]

# Step 2: Infinite generator that cycles through tasks
def infinite_task_scheduler(task_list):
    for task in itertools.cycle(task_list):
        # Yield a tuple: (task, lazy_logger function)
        yield task, lambda: f"Executed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Step 3: Use the generator manually with next()
def run_scheduler():
    scheduler = infinite_task_scheduler(tasks)
    for i in range(10):  # Stop after 10 iterations
        task, get_log = next(scheduler)
        print(f"Task {i+1}: {task}")
        
        # Lazy logging: Only when requested
        log = get_log()  # log is generated here, not during yield
        print(f"  → {log}")
        time.sleep(0.5)  # Simulate delay between tasks

# Run it
if __name__ == "__main__":
    run_scheduler()
