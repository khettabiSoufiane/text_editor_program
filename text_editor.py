import tkinter as tk
from tkinter.filedialog import *

# Create the main window
window = tk.Tk()
window.title("soufiane text editor")

# Configure window size
window.rowconfigure(1, minsize=600)
window.columnconfigure(1, minsize=800)

def open_file():
    # Open file dialog to choose a file to open
    filePath = askopenfilename(
        filetypes=[("text file", "*.txt"), ("all file", "*.*")]
    )
    
    # If no file is selected, return
    if not filePath:
        return
    
    # Clear the text editor widget
    txt_edit.delete(1.0, tk.END)
    
    # Read the content of the selected file
    with open(filePath, "r") as input_file:
        text = input_file.read()
        # Insert the file content into the text editor widget
        txt_edit.insert(tk.END, text)

    # Update the window title to include the file path
    window.title(f"soufiane text editor - {filePath}")


def save_as():
    # Open file dialog to choose a file location to save
    filePath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("text file", "*.txt"), ("all file", "*.*")]
    )
    
    # If no file path is chosen, return
    if not filePath:
        return
      
    # Write the content of the text editor to the chosen file location
    with open(filePath, "w") as input_file:
        text = txt_edit.get(1.0, tk.END)
        input_file.write(text) 

    # Update the window title to include the file path
    window.title(f"soufiane text editor - {filePath}") 


def delete_button_clicked():
    # Clear the text editor widget
    txt_edit.delete(1.0, tk.END) 


# Create the text editor widget
txt_edit = tk.Text(window, bg="black", fg="white")
leb_box = tk.Label(window, text="text box", font=20, bg="blue", fg="white")

# Create a frame for buttons
frame_button = tk.Button(window, width=2, height=5, relief=tk.RAISED, bg="blue")
leb_button = tk.Label(frame_button, text="Button", font=20, bg="blue", fg="white")

# Create buttons for open file, save as, and delete actions
openFile_button = tk.Button(frame_button, text="Open File", command=open_file)
saveAs_button = tk.Button(frame_button, text="Save As", command=save_as)
delete_button = tk.Button(frame_button, text="Delete", command=delete_button_clicked)

# Position the widgets using grid layout
leb_box.grid(column=1, row=0, sticky="NSEW", pady=5)
txt_edit.grid(column=1, row=1, sticky="NSEW")

frame_button.grid(column=0, row=0, sticky="NW", padx=5, pady=5)
leb_button.grid(column=0, row=0, sticky="N")
openFile_button.grid(column=0, row=1, sticky="EW")
saveAs_button.grid(column=0, row=2, sticky="EW")
delete_button.grid(column=0, row=3, sticky="EW")

# Start the Tkinter event loop
window.mainloop()
