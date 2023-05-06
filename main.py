import sqlite3 as sq

# в будущем будут реализованы функции редактирования и удаления операции
# и все функции с операциями будут образовывать отдельный класс __operations__
def insert(db_name,table_name):
    date = int(input("Введите дату операции\n"))
    type = input("Введите тип операции\n")
    category = input("Введите категорию операции\n")
    value = int(input("Введите сумму операции\n"))

    cursor = db_name.cursor()
    cursor.execute(f"""INSERT INTO {table_name}(date, type, category, value)
    VALUES({date}, {type}, {category}, {value});
    """)
    db_name.commit()

with sq.connect("finance.db") as con:
    cur = con.cursor()

    # cur.execute("""DROP TABLE IF EXISTS finance""")

    cur.execute("""CREATE TABLE IF NOT EXISTS finance(
    operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    /* хранится в виде секунд */
    date INTEGER,
    /* затраты либо доходы */
    type TEXT,
    /* категория (подарки, продукты ) */
    category TEXT,
    /* значение транзакции */
    value REAL
    )""")

    insert(con,"finance")
