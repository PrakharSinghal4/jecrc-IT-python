lst = [4,5,2,6,2,6,2,5,1,6,4]
max = lst[0]
for i in range(len(lst)):
    if max < lst[i]:
        max = lst[i]
print(max)
