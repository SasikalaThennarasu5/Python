class InvalidCSVFormatError(Exception): pass

def upload_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if ',' not in line:
                    raise InvalidCSVFormatError("Missing comma")
                print(line.strip())
    except (FileNotFoundError, ValueError, InvalidCSVFormatError) as e:
        log(str(e))
    finally:
        print("CSV processing complete")

def log(msg):
    with open("csv_errors.log", "a") as f:
        f.write(msg + "\n")