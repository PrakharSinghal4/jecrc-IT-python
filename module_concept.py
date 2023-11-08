# import test  # Importing another file
from test import (
    mult,
    sum,
)  # --> This can be used to import particular functions from a file

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
result = sum(num1, num2)
print(result)
result2 = mult(num1,num2)
print(result2)

    