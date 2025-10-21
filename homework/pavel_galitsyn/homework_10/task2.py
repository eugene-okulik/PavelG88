def repeat_me(count=1):
    def dec(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
            print("finished")
        return wrapper
    return dec


@repeat_me(count=5)
def func1(text):
    print(text)


func1('print me')
