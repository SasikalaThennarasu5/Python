
class MultiListIterator:
    def __init__(self, list1, list2):
        self.combined = list1 + list2
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.combined):
            value = self.combined[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


if __name__ == "__main__":
    list1 = ["apple", "banana", "cherry"]
    list2 = ["dates", "fig", "grapes"]

    print("Combined List Items:")
    for item in MultiListIterator(list1, list2):
        print(item)
