'''
module to show custom warnings?, information, errors
'''

def show_message(message, flag):
        # information center
        import tkinter
        from tkinter import messagebox
        
        tkinter.Tk().withdraw()
        
        if flag.lower() == 'info':
            messagebox.showinfo("Information", message)
        
        if flag.lower() == 'error':
            messagebox.showerror("ERROR", message)

        if flag.lower() == 'warning':
            messagebox.showwarning("WARNING", message)