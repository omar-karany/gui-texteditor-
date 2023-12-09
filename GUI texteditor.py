import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename



#back code
def open_file():
    try:      #try and exept to test code if there is an eror in openning file
     filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
     if not filepath:
        return
     text_box.delete(1.0, tk.END)
     with open(filepath, "r") as input_file:
        text = input_file.read()
        text_box.insert(tk.END, text)
     window.title(f"Text Editor Application - {filepath}")
    except Exception as e:
     print(f"Error opening file: {e}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_box.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")


#cearte window
window = Tk()


#creat widgets
frame_butons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_butons, text="open", bd=6,fg="red",height=2, width=7,command=open_file)
btn_save = tk.Button(frame_butons, text="save", bd=6,fg="red",height=2, width=7,command=save_file)
text_box = tk.Text(window,width =110, height=45)


#place widgets
btn_open.grid(column=0, row=0, padx=5,pady=5,sticky="nw")
btn_save.grid(column=0, row=1, padx=5,pady=5,sticky="nw")
frame_butons.grid(column=0, row=0, padx=5,pady=20,sticky="nw")
text_box.grid(column=1, row=0, padx=5,pady=20,sticky="n")

#window properties
window.title("Text Editor")
window.geometry("1000x800+10+20")
window.mainloop()