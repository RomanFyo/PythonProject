from tkinter import *
from tkinter import ttk
from window import Window
import functions

import sql_functions as help


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Приложение")
        width = self.winfo_screenwidth() // 2
        height = self.winfo_screenheight() // 2
        self.geometry(
            f"{width}x{height}+{(self.winfo_screenwidth() - width) // 2}+{(self.winfo_screenheight() - height) // 2}")
        self.resizable(True, True)
        self.state("zoomed")
        # self.iconbitmap(icon)
        self.update_idletasks()
        self.put_frames()

    def put_frames(self):
        self.frame_add_form = AddForm(self).place(relx=0, rely=0, relwidth=0.3, relheight=0.75)
        self.frame_table = TableFrame(self).place(relx=0.3, rely=0, relwidth=0.7, relheight=0.75)
        self.frame_statistics = StatisticsFrame(self).place(relx=0.3, rely=0.75, relwidth=0.7, relheight=0.25)
        self.frame_accounts = AccountFrame(self).place(relx=0, rely=0.75, relwidth=0.3, relheight=0.25)

    def refresh(self):
        all_frames = [f for f in self.children]
        for frame in all_frames:
            self.nametowidget(frame).destroy()
        self.put_frames()

class AddForm(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "red"
        self.put_widgets()

    def put_widgets(self):
        # Дата
        self.add_date_entry = Entry(self)
        add_date_label = Label(self, text="Введите дату:")
        self.add_date_entry.place(relx=0.55, rely=0.08, relwidth=0.4, relheight=0.05)
        add_date_label.place(relx=0.02, rely=0.08, relwidth=0.46, relheight=0.05)

        # Тип: доход / расход
        self.add_type_combobox = ttk.Combobox(self, values=["expense", "income"])
        add_type_label = Label(self, text="Выберите тип транзакции:")
        self.add_type_combobox.place(relx=0.55, rely=0.21, relwidth=0.4, relheight=0.05)
        add_type_label.place(relx=0.02, rely=0.21, relwidth=0.46, relheight=0.05)

        # Категория
        self.add_category_combobox = ttk.Combobox(self, values=list(help.get_categories()))
        add_category_label = Label(self, text="Выберите категорию транзакции:")
        self.add_category_combobox.place(relx=0.55, rely=0.34, relwidth=0.4, relheight=0.05)
        add_category_label.place(relx=0.02, rely=0.34, relwidth=0.46, relheight=0.05)

        # Сумма
        self.add_amount_entry = Entry(self)
        add_amount_label = Label(self, text="Введите сумму транзакции:")
        self.add_amount_entry.place(relx=0.55, rely=0.47, relwidth=0.4, relheight=0.05)
        add_amount_label.place(relx=0.02, rely=0.47, relwidth=0.46, relheight=0.05)
            # Счёт списания / зачисления
        self.add_account_combobox = ttk.Combobox(self, values=('sber', 'tink', 'cash', 'invest'))
        add_account_label = Label(self, text="Выберите счет:")
        self.add_account_combobox.place(relx=0.55, rely=0.6, relwidth=0.4, relheight=0.05)
        add_account_label.place(relx=0.02, rely=0.6, relwidth=0.46, relheight=0.05)

        button_submit = Button(self, text='Внести транзакцию', font=('Times', 14), command=self.insert)
        button_submit.place(relx=0.125, rely=0.77, relwidth=0.75, relheight=0.15)

    def insert(self):
        flag = help.insert1(self.add_date_entry, self.add_type_combobox, self.add_category_combobox, self.add_amount_entry,
                            self.add_account_combobox)

        if flag:
            self.master.refresh()

class TableFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "blue"
        self.put_widgets()

    def put_widgets(self):
        table = ttk.Treeview(self, show='headings')
        heads = ['id', 'data', 'type', 'category', 'amount', 'comment']
        table['columns'] = heads

        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center', width=200)

        for row in help.get_data('finance.db', 'financeData'):
            table.insert('', END, values=row)

        scroll_pane = ttk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=RIGHT, fill=Y)

        table.pack(expand=YES, fill=BOTH)


class StatisticsFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "green"
        self.put_widgets()

    def put_widgets(self):
        Label(self, text='Наиболее популярная категория: ' + help.get_most_popular_category(), bg='green',
              borderwidth=3, relief='groove', font=('Times', 14)).grid(row=1, column=1, sticky=NSEW)
        Label(self, text='Наиболее редкая категория: ' + help.get_least_popular_category(), bg='green',
              borderwidth=3, relief='groove', font=('Times', 14)).grid(row=2, column=1, sticky=NSEW)
        Label(self, text='Самый растратный день недели: ' + help.get_most_expensive_day_of_week(),
              bg='green', borderwidth=3, relief='groove', font=('Times', 14)).grid(row=3, column=1, sticky=NSEW)
        Label(self, text='Сумма расходов в текущем месяце: ' + str(help.get_expenses_in_current_month()),
              bg='green', borderwidth=3, relief='groove', font=('Times', 14)).grid(row=1, column=2, sticky=NSEW)
        Label(self, text='Средняя сумма расходов в месяц: ' + str(help.get_mean_expenses_per_month()),
              bg='green', borderwidth=3, relief='groove', font=('Times', 14)).grid(row=2, column=2, sticky=NSEW)
        Label(self, text='Средняя сумма доходов в месяц: ' + str(help.get_mean_income_per_month()),
              bg='green', borderwidth=3, relief='groove', font=('Times', 14)).grid(row=3, column=2, sticky=NSEW)

        self.grid_columnconfigure(ALL, weight=1)
        self.grid_rowconfigure(ALL, weight=1)


class AccountFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "purple"
        self.put_widgets()

    def put_widgets(self):
        accounts = help.count_budget()
        label_general_balance = Label(self, text='Общий баланс: ' + str(sum(accounts.values())), bg='purple',
                                      font=('Times', 14), borderwidth=3, relief='groove', )
        label_general_balance.grid(row=0, column=0, sticky=NSEW, columnspan=2)

        i = 1
        for key in accounts.keys():
            if i == len(accounts.keys()) and (i % 2):
                Label(self, text=key + ': ' + str(accounts[key]), borderwidth=3, relief='groove', bg='cyan',
                      font=('Times', 14)).grid(row=i - int(not i % 2), column=0, sticky=NSEW, columnspan=2)
                break
            Label(self, text=key + ': ' + str(accounts[key]), borderwidth=3, relief='groove',
                  bg=('orange' if i % 2 else 'yellow'), font=('Times', 14)).grid(row=i - int(not i % 2), column=i % 2,
                                                                                 sticky=NSEW)
            i += 1

        self.grid_columnconfigure(ALL, weight=1)
        self.grid_rowconfigure(ALL, weight=1)


app = App()
app.mainloop()