import json
from datetime import datetime

def cli_logger(func):
    def wrapper(*args, **kwargs):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "args": args,
            "kwargs": kwargs
        }
        with open("cli_log.json", "a") as f:
            json.dump(log_entry, f)
            f.write("\n")
        return func(*args, **kwargs)
    return wrapper
