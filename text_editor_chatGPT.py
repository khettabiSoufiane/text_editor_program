import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            editor.delete('1.0', tk.END)
            editor.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(editor.get('1.0', tk.END))

# Create the main window
window = tk.Tk()
window.title("Text Editor")

# Create the text editor widget
editor = tk.Text(window)
editor.grid(row=0, column=0, sticky="nsew")

# Create the menu bar
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the window to use the menu bar
window.config(menu=menu_bar)

# Configure grid weights to make the text editor expandable
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the Tkinter event loop
window.mainloop()
