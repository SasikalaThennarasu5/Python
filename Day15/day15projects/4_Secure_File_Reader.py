def read_file(file_path):
    try:
        try:
            f = open(file_path, 'r')
            if not f.readable():
                raise PermissionError("File not readable")
            content = f.read()
            print(content)
        finally:
            f.close()
    except FileNotFoundError:
        log("File not found")
    except PermissionError as e:
        log(str(e))

def log(msg):
    with open("file_errors.log", "a") as f:
        f.write(msg + "\n")