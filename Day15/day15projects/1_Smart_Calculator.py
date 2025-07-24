class InvalidOperationError(Exception): pass

def calculate(a, b, op):
    try:
        a = float(a)
        b = float(b)
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/': return a / b
        elif op == '%': return a % b
        else: raise InvalidOperationError("Invalid operation.")
    except ZeroDivisionError:
        log_exception("ZeroDivisionError occurred")
    except ValueError:
        log_exception("ValueError: Non-numeric input")
    except InvalidOperationError as e:
        log_exception(str(e))
    finally:
        print("Calculation complete.")

def log_exception(message):
    with open("calc_errors.log", "a") as f:
        f.write(message + "\n")