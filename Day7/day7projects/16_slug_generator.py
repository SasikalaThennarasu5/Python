title = input("Enter blog title: ").strip().lower()
slug = "-".join(title.split())
print("Slug:", slug)