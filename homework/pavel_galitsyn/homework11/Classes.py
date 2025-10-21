class Book:
    material = 'бумага'
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        info = (
            f'Название: {self.title}, Автор: {self.author}, '
            f'страниц: {self.pages}, материал: {self.material}'
        )
        if self.reserved:
            info += ', зарезервирована'
        return info


class SchoolBook(Book):
    def __init__(
        self, title, author, pages, isbn,
        subject, school_class, has_tasks, reserved=False
    ):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_tasks = has_tasks

    def __str__(self):
        info = (
            f'Название: {self.title}, Автор: {self.author}, '
            f'страниц: {self.pages}, предмет: {self.subject}, '
            f'класс: {self.school_class}'
        )
        if self.reserved:
            info += ', зарезервирована'
        return info


book1 = Book('Властелин колец', 'Дж. Р. Р. Толкин', 500, '8845292614')
book2 = Book('Игра престолов', 'Дж. Р. Р. Мартин', 800, '8845293498')
book3 = Book('Ведьмак', 'Анджей Сапковский', 740, '88234293498')
book4 = Book('Хроники Нарнии', 'Клайв Льюис', 980, '90764293498')
book5 = Book('Тёмные начала', 'Филип Пулман', 1400, '90764456498')

sb1 = SchoolBook(
    'Алгебра', 'Иванов', 200, '978-5-17-111111-1',
    'Математика', 9, True
)
sb2 = SchoolBook(
    'История России', 'Петров', 180, '978-5-17-111111-2',
    'История', 8, False
)
sb3 = SchoolBook(
    'География', 'Сидоров', 160, '978-5-17-111111-3',
    'География', 6, True
)

sb2.reserved = True
book3.reserved = True

for book in [book1, book2, book3, book4, book5]:
    print(book)

for sb in [sb1, sb2, sb3]:
    print(sb)
