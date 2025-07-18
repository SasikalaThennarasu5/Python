import os

OUTPUT_DIR = "resumes"

def export_resume(content, filename):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"Resume exported to {path}")