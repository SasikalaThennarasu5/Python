# 15. File Type Counter

files = ["data.csv", "report.doc", "image.png", "summary.doc", "archive.zip"]
counter = {}

for f in files:
    ext = f.split(".")[-1]
    counter[ext] = counter.get(ext, 0) + 1

print("File Type Count:", counter)
