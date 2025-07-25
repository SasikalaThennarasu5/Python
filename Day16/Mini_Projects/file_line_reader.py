
def read_non_empty_lines(filename):
    try:
        with open(filename, 'r') as file:
            file_iter = iter(file)
            while True:
                try:
                    line = next(file_iter).strip()
                    if line:  # Check non-empty after stripping whitespace
                        print(line)
                except StopIteration:
                    break
    except FileNotFoundError:
        print(f" File not found: {filename}")
    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'sample.txt' with your actual file name
    read_non_empty_lines("sample.txt")
