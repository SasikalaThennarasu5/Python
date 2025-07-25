import time
import os

def log_stream_monitor(filepath, keywords=("ERROR", "WARNING")):
    """
    Generator that monitors a file and yields lines containing specific keywords
    as they are appended in real-time.
    """
    with open(filepath, 'r') as file:
        # Go to the end of the file
        file.seek(0, os.SEEK_END)
        
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait before checking again
                continue
            if any(keyword in line for keyword in keywords):
                yield line.strip()

# Example usage
if __name__ == "__main__":
    log_file = "server.log"  # Path to your log file

    try:
        print(" Monitoring log file for ERROR or WARNING... (Ctrl+C to stop)\n")
        for log_line in log_stream_monitor(log_file):
            print(f"  {log_line}")
    except KeyboardInterrupt:
        print("\n Monitoring stopped by user.")
