from tkinter import *
from window_for_entering_transaction import Enter_transaction
# класс для тестирования наложения двух окон
class Window:
    def __init__(self, width, height, title="Блокнот для записи финансов", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+400+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon != None:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()

    def create_enter_transaction_window(self,icon_name=None):
        Enter_transaction(self.root,icon=icon_name)


if __name__ == "__main__":
    icon_name = "icon.ico"
    window = Window(500, 500,icon=icon_name)
    window.create_enter_transaction_window(icon_name)
    # print(window.root.winfo_width())
    window.run()
