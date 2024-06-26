from tkinter import *
from tkinter.ttk import * 
from tkinter.filedialog import asksaveasfile

window = Tk()
window.geometry("300x300")
window.title("Saving a file")


def save():
    files = [("All Files", "*.*"), ("Python Files", "*.py"), ("Text Document", "*.txt")]
    file = asksaveasfile(filetypes = files, defaultextension = files)

    
    
button = Button(window, text = "Save file", command = lambda:save()).place(x = 150, y = 150)



window.mainloop()