def dec(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("finished")

    return wrapper


@dec
def simple():
    print("hello")


simple()
