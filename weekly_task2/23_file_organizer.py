files = input("Enter file names separated by space: ").split()
organized = {}

for f in files:
    ext = f.split('.')[-1]
    organized.setdefault(ext, []).append(f)

for ext, f_list in organized.items():
    print(f"\n.{ext} files:")
    for name in f_list:
        print("-", name)
