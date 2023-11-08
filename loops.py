# Loops in PYTHON
# for i in range(10):
#     print('Hello World')


# name = "Prakhar Singhal"
# for i in name:
#     print(i)


# lst = (1,2,3,4,5,6)
# for i in lst:
#     print(i)


# d = {'a' : 20, 'b':30, 'c':40, 'd':50}
# # for i in d:
# #     print(i) --> keys will be obtained

# for key,values in d.items(): #this will create a tuple for every item (key + value) in the dictionary [i.e. list of tuples]
#     print(key, values)

# lst = [2,5,1,7,4,6,94,6,7,8,22,11,4]
# for i in range(len(lst)):
#     if lst[i] == 8:
#         print(i)
#     else:
#         pass



name = 'upflairs jaipur'
dic = {}
for i in name:
    dic[i] = name.count(i)
print(dic)