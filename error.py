try:
    print('Trying 1 / 0')
    total = 1 / 0
    print('this will not show up')
except Exception:
    print('Exception was run :D')
    total = 0
print(total)
