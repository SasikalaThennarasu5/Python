import importlib
import mymodule
print(mymodule.some_function())
importlib.reload(mymodule)
print(mymodule.some_function())
