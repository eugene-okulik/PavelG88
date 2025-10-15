import sys
sys.set_int_max_str_digits(100000)


def gen_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = gen_fibonacci()

numbers = [5, 200, 1000, 100000]
for i in range(1, max(numbers) + 1):
    num = next(fib)
    if i in numbers:
        print(f'{i} число Фибоначчи: {num}')
