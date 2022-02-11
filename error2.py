num = input('What is a number? ')
try:
    num = int(num)
except Exception as e:
    print('Exception was run')
    print(type(e))
    num = "Unknown"
print(num)
