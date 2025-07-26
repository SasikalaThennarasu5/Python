from datetime import datetime

class SecureData:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        print(f"Accessed at {datetime.now()}")
        return self._data

    @data.setter
    def data(self, value):
        raise AttributeError("Modification not allowed")
