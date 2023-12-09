import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("1000x800+10+20")

        self.create_widgets()

    def open_file(self):
        try:
            filepath = filedialog.askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if not filepath:
                return
            self.text_box.delete(1.0, tk.END)
            with open(filepath, "r") as input_file:
                text = input_file.read()
                self.text_box.insert(tk.END, text)
            self.master.title(f"Text Editor Application - {filepath}")
        except Exception as e:
            print(f"Error opening file: {e}")

    def save_file(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.text_box.get(1.0, tk.END)
            output_file.write(text)
        self.master.title(f"Text Editor Application - {filepath}")

    def create_widgets(self):
        frame_buttons = tk.Frame(self.master, relief=tk.RAISED)
        frame_buttons.grid(column=0, row=0, padx=5, pady=20, sticky="nw")

        btn_open = tk.Button(
            frame_buttons, text="Open", bd=6, fg="red", height=2, width=7, command=self.open_file
        )
        btn_open.grid(column=0, row=0, padx=5, pady=5, sticky="nw")

        btn_save = tk.Button(
            frame_buttons, text="Save", bd=6, fg="red", height=2, width=7, command=self.save_file
        )
        btn_save.grid(column=0, row=1, padx=5, pady=5, sticky="nw")

        self.text_box = tk.Text(self.master, width=110, height=45)
        self.text_box.grid(column=1, row=0, padx=5, pady=20, sticky="n")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
