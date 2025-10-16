import random

user_input = input("Enter your salary: ")
salary = int(user_input)

bonus = random.choice([True, False])

if bonus:
    salary += random.randint(100, 5000)

print(f'{user_input}, {bonus} - "${salary}"')
