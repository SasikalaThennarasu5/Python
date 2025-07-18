import csv, statistics

def generate_summary(file_path):
    with open(file_path, newline='') as csvfile:
        data = [int(row[0]) for row in csv.reader(csvfile)]
        print("Mean:", statistics.mean(data))
        print("Median:", statistics.median(data))
