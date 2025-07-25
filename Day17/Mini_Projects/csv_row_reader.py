
def csv_row_reader(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        next(file)  # Skip header
        for line in file:
            cleaned_line = line.strip()
            if "END" in cleaned_line:
                break
            yield cleaned_line

if __name__ == "__main__":
    file_path = "products.csv"  # Ensure this file exists in the same directory
    print("Reading CSV rows lazily:\n")
    for row in csv_row_reader(file_path):
        print(row)
