'''
module to show custom warnings, information, errors
'''
import tkinter
from tkinter import messagebox

DEFAULT = "INFO"
INFO    = "INFO"
ERROR   = "ERROR"
WARNING = "WARNING"

def show_message(message, flag="INFO"):
        # information center
        window = tkinter.Tk()
        window.withdraw()

        if flag.upper() == INFO:
            messagebox.showinfo("Information", message)
        
        if flag.upper() == ERROR:
            messagebox.showerror("ERROR", message)

        if flag.upper() == WARNING:
            messagebox.showwarning("WARNING", message)