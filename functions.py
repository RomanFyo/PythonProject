from tkinter import *
from tkinter import messagebox as mb
import sql_functions as help


def get_date(date):
    separated_date = max([date.get().split("."), date.get().split("/")], key=lambda x: len(x))
    try:
        list(map(int, separated_date))
        if len(separated_date) != 3 or len(separated_date[0]) != 2 or len(separated_date[1]) != 2 or len(separated_date[2]) != 4:
            raise ValueError()
        return ".".join(separated_date)
    except ValueError:
        mb.showerror(
            "Ошибка",
            "Некорректный ввод данных (дата)"
        )
        return None

def get_category(category):
    if category.get() in list(help.get_categories()):
        return category.get()
    mb.showerror(
        "Ошибка",
        "некорректный ввод данных (категория)"
    )
    return None

def get_type(type):
    if type.get() in ["income", "expense"]:
        return type.get()
    mb.showerror(
        "Ошибка",
        "Некорректный ввод данных (тип транзакции)"
    )
    return None

def get_amount(amount):
    try:
        amount = float(amount.get())
        return amount
    except ValueError:
        mb.showerror(
            "Ошибка",
            "Некорректный ввод данных (сумма)"
        )
        return None


def get_account(account):
    if account.get() in ("sber", "tink", "cash", "invest"):
        return account.get()
    mb.showerror(
        "Ошибка",
        "Некорректный ввод данных (счет)"
    )
    return None