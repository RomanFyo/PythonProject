from tkinter import *

class Window:
    def __init__(self, width=None, height=None, title='Title', resizable=(False,False),icon=None):
        self.root = Tk()
        self.root.title(title)
        if width is None:
            width = self.root.winfo_screenwidth() // 2
        if height is None:
            height = self.root.winfo_screenheight() // 2
        self.root.geometry(f"{width}x{height}+{(self.root.winfo_screenwidth()-width)//2}+{(self.root.winfo_screenheight()-height)//2}")
        self.root.resizable(resizable[0], resizable[1])

        if icon:
            self.root.iconbitmap(icon)

        self.root.update_idletasks()

    def get_root(self):
        return self.root