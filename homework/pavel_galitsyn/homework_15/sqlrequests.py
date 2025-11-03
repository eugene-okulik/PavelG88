import mysql.connector as mysql

# 1️⃣ Подключение к базе
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# === Добавляем студента ===
cursor.execute("""
    INSERT INTO students (name, second_name)
    VALUES ('Robert', 'De Niro')
""")
student_id = cursor.lastrowid
print(f"Добавлен студент Robert De Niro (id = {student_id})")

# === Добавляем группу ===
cursor.execute("""
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES ('Actors_Group_2025', '2025-11-02', '2026-05-15')
""")
group_id = cursor.lastrowid
print(f"Добавлена группа Actors_Group_2025 (id = {group_id})")

# === Назначаем студента в группу ===
cursor.execute("""
    UPDATE students
    SET group_id = %s
    WHERE id = %s
""", (group_id, student_id))
print(f"Студент {student_id} добавлен в группу {group_id}")

# === Добавляем книги и выдаем студенту ===
books = [
    ("Acting Techniques", student_id),
    ("Film Directing Basics", student_id),
    ("Stanislavski Method", student_id)
]
cursor.executemany("""
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
""", books)
print("Книги выданы студенту")

# === Добавляем предметы ===
subjects = ["Acting", "Cinematography", "Film History"]
subject_ids = []
for subj in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subj,))
    subject_ids.append(cursor.lastrowid)
print("Добавлены предметы:", subjects)

# === Добавляем уроки по каждому предмету ===
lessons_data = []
for subj_id, subj_name in zip(subject_ids, subjects):
    cursor.executemany("""
        INSERT INTO lessons (title, subject_id)
        VALUES (%s, %s)
    """, [
        (f"Introduction to {subj_name}", subj_id),
        (f"Advanced {subj_name}", subj_id)
    ])
print("Уроки созданы для всех предметов")

# === Получаем все уроки для выставления оценок ===
cursor.execute("SELECT id, title FROM lessons WHERE subject_id IN (%s, %s, %s)", tuple(subject_ids))
lessons = cursor.fetchall()

# === Добавляем оценки студенту ===
marks_data = [
    (5, lessons[0]['id'], student_id),
    (4, lessons[1]['id'], student_id),
    (5, lessons[2]['id'], student_id),
    (3, lessons[3]['id'], student_id),
    (5, lessons[4]['id'], student_id),
    (4, lessons[5]['id'], student_id)
]
cursor.executemany("""
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
""", marks_data)
print("Добавлены оценки студенту")

# === Выводим итоговую сводку ===
cursor.execute("""
SELECT
    s.name AS student_name,
    s.second_name AS student_second_name,
    g.title AS group_title,
    b.title AS book_title,
    sub.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = %s
ORDER BY sub.title, l.title
""", (student_id,))

summary = cursor.fetchall()

print("\nИтоговая информация о студенте Robert De Niro:")
for row in summary:
    print(
        f"Студент: {row['student_name']} {row['student_second_name']} | "
        f"Группа: {row['group_title']} | "
        f"Книга: {row['book_title']} | "
        f"Предмет: {row['subject_title']} | "
        f"Урок: {row['lesson_title']} | "
        f"Оценка: {row['mark']}"
    )

db.commit()
db.close()
print("\nВсе операции успешно выполнены.")
