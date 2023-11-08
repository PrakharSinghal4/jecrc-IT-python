lst = list(range(1,21))


def squa(x):
    return x**2

# print(list(map(squa,lst)))

print(list(filter(lambda x: x%2==0, lst)))