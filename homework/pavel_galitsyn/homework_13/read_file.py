import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))

file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

now = datetime.datetime.now()

with open(file_path, encoding='utf-8-sig') as f:
    for line in f:
        parts = line.split(' - ')
        date_str = parts[0].split('. ', 1)[1]
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        number = int(line.split('.')[0])

        if number == 1:
            print(date_obj + datetime.timedelta(days=7))
        elif number == 2:
            print(date_obj.strftime('%A'))
        elif number == 3:
            difference = now - date_obj
            print(f'Эта дата была {difference.days} дней назад')
