class Flower:
    def __init__(self, name, color, stem_length, price, life_time):
        self.name = name
        self.color = color
        self.stem_length = stem_length  # длина стебля
        self.price = price
        self.life_time = life_time  # срок жизни (в днях)

    def __str__(self):
        return (
            f"{self.name}, {self.color}, {self.stem_length}см, "
            f"{self.price}$, живет {self.life_time} дн."
        )


class Rose(Flower):
    def __init__(self, name, color, stem_length, price, life_time, sort):
        super().__init__(name, color, stem_length, price, life_time)
        self.sort = sort

    def __str__(self):
        return (
            f"{self.name}, {self.color}, {self.stem_length}см, "
            f"{self.price}$, живет {self.life_time} дн. сорт: {self.sort}"
        )


class Tulip(Flower):
    def __init__(self, name, color, stem_length, price, life_time, bulb):
        super().__init__(name, color, stem_length, price, life_time)
        self.bulb = bulb

    def __str__(self):
        return (
            f"{self.name}, {self.color}, {self.stem_length}см, "
            f"{self.price}$, живет {self.life_time} дн. вид луковицы: {self.bulb}"
        )


class Chamomile(Flower):
    def __init__(self, name, color, stem_length, price, life_time, kind):
        super().__init__(name, color, stem_length, price, life_time)
        self.kind = kind

    def __str__(self):
        return (
            f"{self.name}, {self.color}, {self.stem_length}см, "
            f"{self.price}$, живет {self.life_time} дн. тип: {self.kind}"
        )


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        return sum(f.price for f in self.flowers)

    def average_life_time(self):
        return sum(f.life_time for f in self.flowers) / len(self.flowers)

    def sort_by(self, key):
        self.flowers.sort(key=lambda f: getattr(f, key))

    def find_by_life_time(self, min_days):
        return [f for f in self.flowers if f.life_time >= min_days]

    def __str__(self):
        return "\n".join(str(f) for f in self.flowers)


rose = Rose("Роза", "красная", 50, 300, 7, "чайная")
tulip = Tulip("Тюльпан", "желтый", 40, 150, 5, "крупная")
chamomile = Chamomile("Ромашка", "белая", 30, 100, 4, "полевая")

bouquet = Bouquet([rose, tulip, chamomile])

print("Состав букета:")
print(bouquet)

print("\nОбщая стоимость:", bouquet.total_price(), "$")
print("Среднее время жизни:", bouquet.average_life_time(), "дн.")

bouquet.sort_by("price")
print("\nСортировка по цене:")
print(bouquet)

found = bouquet.find_by_life_time(5)
print("\nЦветы, живущие 5+ дней:")
for f in found:
    print(f)
