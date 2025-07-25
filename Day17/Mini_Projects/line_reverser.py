def reverse_lines(filepath):
    """
    Generator that reads each line from a file,
    strips the newline character, and yields the reversed line.
    """
    try:
        with open(filepath, 'r') as file:
            for line in file:
                yield line.strip()[::-1]
    except FileNotFoundError:
        print(f" File not found: {filepath}")

# Example usage
def main():
    filepath = "sample.txt"  # Change this to your filename

    print(" Reversed Lines:\n")
    for reversed_line in reverse_lines(filepath):
        print(reversed_line)

if __name__ == "__main__":
    main()
