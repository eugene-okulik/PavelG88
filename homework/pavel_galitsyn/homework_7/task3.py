def result(text):
    number = text.split(': ')[1]
    number = int(number)
    print(number + 10)

result("результат операции: 42")
result("результат операции: 54")
result("результат работы программы: 209")
result("результат: 2")
