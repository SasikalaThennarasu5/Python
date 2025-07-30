import tkinter as tk
from tkinter import filedialog, messagebox
from functools import wraps
import os

recent_files = []

def autosave(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(self.text_area.get(1.0, tk.END))
        return result
    return wrapper

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Text Editor")
        self.text_area = tk.Text(root, wrap='word')
        self.text_area.pack(expand=1, fill='both')
        self.file_path = ""

        self._create_menu()

    def _create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Find and Replace", command=self.find_replace)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menu_bar)

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
                self.file_path = path
                recent_files.append(path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    @autosave
    def save_file(self):
        if self.file_path:
            return
        self.save_file_as()

    def save_file_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Documents", "*.txt")])
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.text_area.get(1.0, tk.END))
                self.file_path = path
                recent_files.append(path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def find_replace(self):
        find = simpledialog.askstring("Find", "Enter word to find:")
        replace = simpledialog.askstring("Replace", "Enter replacement:")
        if find and replace:
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find, replace)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, new_content)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
