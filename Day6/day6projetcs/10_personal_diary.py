# Personal Diary Entry Tool
def diary(entry):
    def save():
        print("Entry saved:", entry)
    save()
    return len(entry), len(entry.split())

length, words = diary("Today was a good day. I learned Python.")
print("Length:", length, "| Word Count:", words)
