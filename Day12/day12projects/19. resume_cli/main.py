
from resume.input import collect_input, load_input
from resume.template import generate_text, generate_markdown
from resume.export import export_resume

def main():
    data = load_input()
    if not data:
        data = collect_input()

    print("\nChoose output format:")
    print("1. Plain Text")
    print("2. Markdown")
    choice = input("Option: ")

    if choice == "1":
        content = generate_text(data)
        export_resume(content, "resume.txt")
    elif choice == "2":
        content = generate_markdown(data)
        export_resume(content, "resume.md")

if __name__ == "__main__":
    main()
