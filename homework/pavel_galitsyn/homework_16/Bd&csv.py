import csv
import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

with open(
    r'D:\Work\GitProject\PavelG88\homework\eugene_okulik\Lesson_16\data.csv',
    newline='',
    encoding='utf-8-sig'
) as csv_file:
    file_data = csv.reader(csv_file)
    not_found = []

    for row in file_data:
        last, name, city = row
        query = """
        SELECT * FROM students
        WHERE second_name = %s AND name = %s
        """
        cursor.execute(query, (last, name))
        result = cursor.fetchall()

        if not result:
            not_found.append(row)

if not_found:
    print("В базе отсутствуют такие записи:")
    for row in not_found:
        print(row)
else:
    print("Все записи из CSV есть в базе данных.")
