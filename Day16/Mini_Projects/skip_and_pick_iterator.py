class SkipAndPickIterator:
    def __init__(self, data_list):
        self.data = data_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 2  # skip every alternate item
        return item


if __name__ == "__main__":
    user_input = input("Enter list items separated by space: ").split()
    iterator = SkipAndPickIterator(user_input)

    print("\n Picked elements (skipping alternates):")
    for item in iterator:
        print(item, end=' ')
