# print('program execution start')


# try:
#     num = int(input('Enter first number : '))
#     num2 = int(input('Enter second number : '))
#     result = num / num2
#     print(result)


# except Exception as a:
#     print('Zero divison error')
#     # print(e) --> Division by zero (error message automatically detected)

# else:
#     print('Exception not occured.')
# finally:
#     print('Will always run')
# print('program execution finished.')


try:
    num = int(input('Enter a number : '))
    print(num)
    print('hi')
except IndentationError:
    print("Please fix the syntax")
except Exception as e:
    print('Entered number is not of type int')



# in Except block error category can also be mentioned. 
# except ValueError:
    # print("Error")