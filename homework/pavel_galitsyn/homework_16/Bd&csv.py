import csv
import os

import dotenv
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(
    base_dir, "..", "..", "eugene_okulik", "Lesson_16", "hw_data", "data.csv"
)
csv_path = os.path.abspath(csv_path)

with open(csv_path, newline="", encoding="utf-8-sig") as csv_file:
    file_data = csv.reader(csv_file)
    not_found = []

    for row in file_data:
        (
            name,
            second_name,
            group_title,
            book_title,
            subject_title,
            lesson_title,
            mark_value
        ) = row

        query = """
        SELECT m.id
        FROM marks m
        JOIN students s ON m.student_id = s.id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects sub ON l.subject_id = sub.id
        JOIN books b ON b.taken_by_student_id = s.id
        JOIN `groups` g ON s.group_id = g.id
        WHERE s.name = %s
          AND s.second_name = %s
          AND g.title = %s
          AND b.title = %s
          AND sub.title = %s
          AND l.title = %s
          AND m.value = %s
        """

        cursor.execute(
            query,
            (
                name,
                second_name,
                group_title,
                book_title,
                subject_title,
                lesson_title,
                mark_value
            )
        )
        result = cursor.fetchall()

        if not result:
            not_found.append(row)

if not_found:
    print("В базе отсутствуют такие записи:")
    for row in not_found:
        print(row)
else:
    print("Все записи из CSV есть в базе данных.")
