# temp = []
# for i in range(1,11):
#     temp.append(i**2)
# print(temp)

# print()

# lst_of_square = [i**2 for i in range(1,11)]
# print(lst_of_square)


# lst = [i for i in range(1,21)]
# print(lst)


# evens = []
# for i in range(1,50):
#     if i%2==0:
#         evens.append(i)
# print(evens)

# evens = [i for i in range(1,50) if i%2==0] -> This syntax will be used if we only want 'if' in out list comprehension
# print(evens)

# evens = [
#     i if i % 2 == 0 else "odd" for i in range(1, 50)
# ]  # This syntax will be used if we want both if and else
# print(evens)


lst = [[i for i in range(1,4)] for i in range(1,5)]
print(lst)  #NESTED LIST COMPREHENSION

lst = list(range(1,21))
print(lst)

