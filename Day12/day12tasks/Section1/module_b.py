import module_a

def function_b():
    print("Function B from module B")
    module_a.function_a()

if __name__ == "__main__":
    function_b()
