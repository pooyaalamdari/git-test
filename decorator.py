def myfunc():
    print('My name is Pooya')

def my_decorator(func):
    def wrapper():
        print('Do something here')
        func()
        print('origin function is finished')
    return wrapper

new_func = my_decorator(myfunc)
new_func()
