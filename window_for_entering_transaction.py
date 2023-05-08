from tkinter import *


class Enter_transaction:
    def __init__(self, parent,icon=None):
        self.root = Toplevel(parent)
        self.root.title("Ввод транзакции")
        self.root.geometry(f"400x400+{int((self.root.winfo_screenwidth()-400)/2)}+{int((self.root.winfo_screenheight()-400)/2)}")
        self.root.resizable(False,False)
        if icon != None:
            self.root.iconbitmap(icon)

        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()