text = input("Enter paragraph: ")
keyword = input("Enter keyword to highlight: ")
highlighted = text.replace(keyword, keyword.upper())
count = text.lower().count(keyword.lower())
print("Highlighted Text:", highlighted)
print("Occurrences:", count)