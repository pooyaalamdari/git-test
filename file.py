my_file = open('data.txt', 'r')
file_content = my_file.read()
my_file.close()
print(file_content)


user_name = input('Enter your name: ')
#w operation write new content and delete past content
#be CAREFUL
my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)
my_file_writing.close()
