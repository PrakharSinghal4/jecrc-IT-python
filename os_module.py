# OS MODULE

import os
# print(os.getcwd())

os.listdir()

# os.mkdir('JECRC')

os.chdir('C:\\Users\\prakh\\OneDrive\\Desktop\\python IT jecrc\\JECRC')

print(os.getcwd())

# open('raj1','r')
# open('raj1','w')
# open('raj2','a')
# open('raj3','x')
# file = open('raj.txt','w')
# message = 'hello jecrc'
# file.write(message) #printing this will give the string length
# file.close()

# file = open('raj.txt','r')
# message = file.read()
# print(message)
# file.close()

# file = open('raj.txt','w') #Write replaces the already existing test
# message = 'this is my class'
# file.write(message) #printing this will give the string length
# file.close()

# file = open('raj.txt','r')
# message = file.read()
# print(message)
# file.close()

# file = open('raj.txt','a')
# message = ' Hello World'
# file.write(message)
# file.close()


# file = open('raj.txt','r')
# message = file.read()
# print(message)
# file.close()

print(os.listdir())

# os.mkdir('Hello')

# os.rename('Hello','Hii')

# print(os.path.exists('Hii'))

if os.path.exists('raj4.txt'):
    pass
else:
    file = open('raj4.txt','x')

# import shutil




import random

# print(random.randint(1,10))
# print(random.random()) --> print a random float number less than 1

lst = list(range(1,21))

random.shuffle(lst)
print(lst)

print(random.choice(lst)) #prints a random number from a list

