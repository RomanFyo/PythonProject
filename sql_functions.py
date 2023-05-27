import sqlite3 as sql
import random
from datetime import *
import functions


def get_most_popular_category():
    data = get_expenses('finance.db', 'financeData')
    quantity = {}
    for row in data:
        if row[3] in quantity:
            quantity[row[3]]['count']+=1
        else:
                quantity[row[3]] = {'count':1, 'name':row[3]}
    return max(quantity.values(), key=lambda x:x['count'])['name']


def get_least_popular_category():
    data = get_expenses('finance.db', 'financeData')
    quantity = {}
    for row in data:
        if row[3] in quantity:
            quantity[row[3]]['count'] += 1
        else:
            quantity[row[3]] = {'count': 1, 'name': row[3]}
    return min(quantity.values(), key=lambda x: x['count'])['name']


def day_of_week(date):
    days={0:"Monday", 1:"Tuesday", 2:"Wensday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    date_split = date.split('.')
    return days[datetime.weekday(datetime(int(date_split[2]), int(date_split[1]), int(date_split[0])))]


def get_random_date(start, end):
    delta = end - start
    result = start + timedelta(random.randint(0, delta.days))
    return  ".".join(str(result).split()[0].replace('-','.').split('.')[::-1])


def get_most_expensive_day_of_week():
    data = get_data('finance.db','financeData')
    quantity = {}
    for row in data:
        current = day_of_week(row[1])
        if current in quantity:
            quantity[current]['count'] += 1
        else:
            quantity[current] = {'count': 1, 'name': current}
    return max(quantity.values(), key=lambda x: x['count'])['name']


def get_expenses_in_current_month():
    data = get_expenses('finance.db','financeData')
    ans = 0
    for row in data:
        if int(row[1].split('.')[1]) == datetime.now().month and int(row[1].split('.')[2]) == datetime.now().year:
            ans += row[4]
    return ans


def get_mean_expenses_per_month():
    data = get_expenses('finance.db', 'financeData')
    quantity = {}
    ans = 0
    for row in data:
        if row[1][3:] in quantity:
            quantity[row[1][3:]]['sum']+=float(row[4])
        else:
            quantity[row[1][3:]] = {'sum':float(row[4])}

    for month in quantity:
        ans += quantity[month]['sum']

    return round(ans / len(quantity), 2)


def get_mean_income_per_month():
    data = get_incomes('finance.db', 'financeData')
    quantity = {}
    ans = 0
    for row in data:
        if row[1][3:] in quantity:
            quantity[row[1][3:]]['count'] += 1
            quantity[row[1][3:]]['sum'] += float(row[4])
        else:
            quantity[row[1][3:]] = {'count': 1, 'sum': float(row[4])}

    for month in quantity:
        ans += quantity[month]['sum'] / quantity[month]['count']

    return round(ans, 2)

def get_categories():
    data = get_data('finance.db', "financeData")
    categories=set()
    for row in data:
        categories.add(row[3])
    return categories

def count_budget():
    data = get_data('finance.db','financeData')
    accounts = {'sber':0, 'tink':0, 'cash':0, 'invest':0}
    for row in data:
        if row[2] == 'income':
            accounts[row[5]] += float(row[4])
        else:
            accounts[row[5]] -= float(row[4])
    return accounts

def insert1(add_date_entry, add_type_combobox, add_category_combobox, add_amount_entry, add_account_combobox):
    date = functions.get_date(add_date_entry)
    type = functions.get_type(add_type_combobox)
    category = functions.get_category(add_category_combobox)
    amount = functions.get_amount(add_amount_entry)
    account = functions.get_account(add_account_combobox)

    if not(None in [date, type, category, amount, account]):
        insert2('finance.db', 'financeData', date, type, category, amount, account)
        return True
    return False

def insert2(db_name, table_name, date, type, category, amount, account, comment='-'):
    con = sql.connect(db_name)
    cursor = con.cursor()
    cursor.execute(f'''INSERT INTO {table_name}(date, type, category, amount, account, comment)
    VALUES("{date}", "{type}", "{category}", {amount},"{account}", "{comment}");
    ''')
    con.commit()


def get_data(db_name,table_name):
    con = sql.connect(db_name)
    cur = con.cursor()
    cur.execute(f'''SELECT * FROM {table_name}''')
    return cur.fetchall()


def get_expenses(db_name,table_name):
    con = sql.connect(db_name)
    cur = con.cursor()
    cur.execute(f'''SELECT * FROM {table_name} WHERE type="expense";''')
    return cur.fetchall()


def get_incomes(db_name,table_name):
    con = sql.connect(db_name)
    cur = con.cursor()
    cur.execute(f'''SELECT * FROM {table_name} WHERE type="income";''')
    return cur.fetchall()