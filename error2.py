num = input('Enter a first number: ')
num2 = input('Enter a seccond number: ')
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2

#if num or num2 are invalid number ValueError will running
except ValueError:
    print(f'{num} or {num2} was not a valid number')

#if num2 is for example number but we get error
#this line will be run
except Exception as e:
    print('Exception was run')
    print(type(e))
