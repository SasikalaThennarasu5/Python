import difflib
import os

def load_document(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""

def yield_matches(base_doc, docs):
    for doc_path in docs:
        content = load_document(doc_path)
        if not content:
            continue
        matcher = difflib.SequenceMatcher(None, base_doc, content)
        ratio = matcher.ratio()
        yield doc_path, round(ratio * 100, 2)

if __name__ == "__main__":
    base_path = input("Enter base document path: ")
    base_content = load_document(base_path)

    if not base_content.strip():
        print("Base document is empty or unreadable.")
    else:
        folder = input("Enter folder containing documents to compare: ")
        all_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".txt") and os.path.join(folder, f) != base_path]

        print("\nPlagiarism Match Percentages:")
        for file, match in yield_matches(base_content, all_files):
            print(f"{file}: {match}%")
