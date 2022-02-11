
def my_decorator(func):
    def wrapper():
        print('Do something here')
        func()
        print('origin function is finished')
    return wrapper

#if we remove decorator (my_decorator)
# @my_decorator
def myfunc():
    print('My name is Pooya')

#we don't need this anymore
# [new_func = my_decorator(myfunc)]
#bcz we use decorator

myfunc()
