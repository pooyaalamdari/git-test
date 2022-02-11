num = input('What is a number? ')
try:
    num = int(num)
#if we got error ValueError block will run
except ValueError:
    print(num, 'was not a valid number')
# these are will not run
except Exception as e:
    print('Exception was run')
    print(type(e))
    num = "Unknown"
print(num)
