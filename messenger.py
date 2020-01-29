'''
module to show custom warnings?, information, errors
'''
class Messenger:
    
    '''
    class to inform user about warnings, information, errors etc
    '''

    DEFAULT = "INFO"
    INFO    = "INFO"
    ERROR   = "ERROR"
    WARNING = "WARNING"

    @staticmethod
    def show_message(message, flag=Messenger.DEFAULT):
            # information center
            import tkinter
            from tkinter import messagebox
            
            tkinter.Tk().withdraw()
            
            if flag.lower() == Messenger.INFO:
                messagebox.showinfo("Information", message)
            
            if flag.lower() == Messenger.ERROR:
                messagebox.showerror("ERROR", message)

            if flag.lower() == Messenger.WARNING:
                messagebox.showwarning("WARNING", message)