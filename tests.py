import random
from sql_functions import *
from datetime import datetime

print(sum({'a':10, 'b':17}.values()))

# создание случаных данных

# for i in range(17):
#     date = get_random_date(datetime.strptime('23.05.2023', '%d.%m.%Y'), datetime.strptime('26.05.2023', '%d.%m.%Y'))
#     type = random.choice(['expense', 'income'])
#     category = random.choice(['food', 'books', 'presents', 'homegoods', 'education'])
#     amount = random.randint(100, 1000)
#     account = random.choice(['sber', 'tink', 'cash', 'invest'])
#     comment = 'Рома гей'
#
#     insert(
#         'finance.db',
#         'financeData',
#         date, type,
#         category, amount,
#         account, comment
#     )

# print(get_data('finance.db', 'financeData'))
