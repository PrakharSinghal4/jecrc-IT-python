# def add_two_num():
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     print("Addition is -> ")
#     return a + b


# print(add_two_num())


# def add_two_num(num1, num2):
#     print("Addition is -> ")
#     return num1 + num2


# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# print(add_two_num(a, b))
# print(11, "\n")


# def find_even(lst):
#     even = []
#     for i in lst:
#         if i % 2 == 0:
#             even.append(i)
#     print(even)


# lst = [1, 2, 6, 4, 3, 7, 5, 1, 6, 9, 4]

# find_even(lst)


# def find_even(lst):
#     for i in lst:
#         if i % 2 == 0:   
#             print(i,end=' ')


# lst = [1, 2, 6, 4, 3, 7, 5, 1, 6, 9, 4]

# find_even(lst)

# def count(name):
#     dic = {}
#     for i in name:
#         dic[i] = name.count(i)
#     print(dic)


# name = "upflairs jaipur"
# count(name)



# find_even(lst)

# def count(name):
#     dic = {}
#     for i in name:
#         dic[i] = name.count(i)
#     print(dic)


# name = "upflairs jaipur"
# count(name)


# add = lambda x,y : x + y

# a = add(3,4)
# print(a)

check_even = lambda x : "Even" if x%2==0 else "Odd"

a = check_even(5)
print(a)
