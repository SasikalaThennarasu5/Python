
import os
from typing import Generator

def scan_directory_txt_files(path: str, max_files: int = 10) -> Generator[str, None, int]:
    """
    Recursively scans a directory for `.txt` files and yields up to `max_files` files.
    Returns the number of files yielded using StopIteration.value
    """
    count = 0
    all_files = (
        os.path.join(root, file)
        for root, _, files in os.walk(path)
        for file in files
        if file.endswith(".txt")
    )

    for file_path in all_files:
        yield file_path
        count += 1
        if count >= max_files:
            break

    return count  # returned with StopIteration when done

if __name__ == "__main__":
    directory = "./test_folder"  # change as needed
    scanner = scan_directory_txt_files(directory, max_files=5)

    print(" Scanned .txt files:\n")
    try:
        while True:
            print(next(scanner))
    except StopIteration as e:
        print(f"\n Finished scanning. Total .txt files found: {e.value}")
