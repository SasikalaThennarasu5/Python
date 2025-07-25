# Generator 1: Raw data
def raw_data():
    for i in range(1, 21):
        yield i

# Generator 2: Filter data (even numbers only)
def filter_data(source_gen):
    for item in source_gen:
        if item % 2 == 0:
            yield item

# Generator 3: Transform data (square the number)
def transform_data(filtered_gen):
    for item in filtered_gen:
        yield item ** 2

# Main pipeline
def main():
    print(" Final Processed Data (even numbers squared):\n")
    for result in transform_data(filter_data(raw_data())):
        print(result)

if __name__ == "__main__":
    main()
