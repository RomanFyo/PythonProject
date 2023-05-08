import sqlite3 as sq
from tkinter import *
from window import Window

root = Window(resizable=(True, True)).get_root()

# разметка основного окна по секциям

frame_add_form = Frame(root, bg='red')
frame_table = Frame(root, bg='blue')
frame_statistics = Frame(root, bg='green')
frame_accounts = Frame(root, bg='purple')

frame_add_form.place(relx=0, rely=0, relwidth=0.3, relheight=0.75)
frame_table.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.75)
frame_statistics.place(relx=0.3, rely=0.75, relwidth=0.7, relheight=0.25)
frame_accounts.place(relx=0, rely=0.75, relwidth=0.3, relheight=0.25)


# секция добавления новой информации

button_date = Button(frame_add_form, text="Введите дату транзакции")
button_type = Button(frame_add_form, text="Введите сумму транзакции")
button_amount = Button(frame_add_form, text="Введите категорию транзакции")
button_account = Button(frame_add_form, text="Выберите карту или счёт")
button_submit = Button(frame_add_form, text="Внести транзакцию")

button_date.place(relx=0.125, rely=0.025, relwidth=0.75, relheight=0.15)
button_type.place(relx=0.125, rely=0.225, relwidth=0.75, relheight=0.15)
button_amount.place(relx=0.125, rely=0.425, relwidth=0.75, relheight=0.15)
button_account.place(relx=0.125, rely=0.625, relwidth=0.75, relheight=0.15)
button_submit.place(relx=0.125, rely=0.825, relwidth=0.75, relheight=0.15)


# секция информации о балансе на отдельных счетах

label_general_balance = Label(frame_accounts, text="Общий баланс - 0", bg="purple")
label_general_balance.grid(row=0, column=0, sticky=NSEW, columnspan=2)
accounts = dict(sber=100, tink=200, nal=300, invest=500, test=0)

i = 1
for key in accounts.keys():
    if i == len(accounts.keys()) and (i % 2):
        Label(frame_accounts, text=key + ": " + str(accounts[key]), bg="cyan").grid(row=i - int(not i%2), column=0, sticky=NSEW, columnspan=2)
        break
    if i%2:
        Label(frame_accounts, text=key + ": "+str(accounts[key]), bg="yellow").grid(row=i - int(not i%2), column=i%2, sticky=NSEW)
    else:
        Label(frame_accounts, text=key + ": "+str(accounts[key]), bg="orange").grid(row=i - int(not i%2), column=i%2, sticky=NSEW)
    i+=1

frame_accounts.grid_columnconfigure(ALL, weight=1)
frame_accounts.grid_rowconfigure(ALL, weight=1)

# если понадобится разметка для 4
# button_date.place(relx=0.125, rely=0.075, relwidth=0.75, relheight=0.175)
# button_type.place(relx=0.125, rely=0.3, relwidth=0.75, relheight=0.175)
# button_amount.place(relx=0.125, rely=0.525, relwidth=0.75, relheight=0.175)
# button_submit.place(relx=0.125, rely=0.75, relwidth=0.75, relheight=0.175)
root.mainloop()


# в будущем будут реализованы функции редактирования и удаления операции
# и все функции с операциями будут образовывать отдельный класс __operations__
# def insert(db_name,table_name):
#     date = int(input("Введите дату операции\n"))
#     type = input("Введите тип операции\n")
#     category = input("Введите категорию операции\n")
#     value = int(input("Введите сумму операции\n"))
#
#     cursor = db_name.cursor()
#     cursor.execute(f"""INSERT INTO {table_name}(date, type, category, value)
#     VALUES({date}, {type}, {category}, {value});
#     """)
#     db_name.commit()
#
# with sq.connect("finance.db") as con:
#     cur = con.cursor()
#
#     # cur.execute("""DROP TABLE IF EXISTS finance""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS finance(
#     operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     /* хранится в виде секунд */
#     date INTEGER,
#     /* затраты либо доходы */
#     type TEXT,
#     /* категория (подарки, продукты ) */
#     category TEXT,
#     /* значение транзакции */
#     value REAL
#     )""")
#
#     insert(con,"finance")


