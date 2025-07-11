quote = input("Enter a multi-line quote (use \n for new lines): ").strip()
lines = quote.count("\n") + 1
print("Cleaned Quote:")
print(quote)
print("Total lines:", lines)