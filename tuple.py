# TUPLE
t1 = (2, 5.5, 6, "a", "Hello")
print(t1)  # (2, 5.5, 6, 'a', 'Hello')
print(len(t1))  # 5
print(t1[0])  # 2
print(t1[4][4])
t2 = (3, 5, 4, "Jecrc")
t3 = t1 + t2
print(t3)
# t1.append(20) Error because tuple is immutable

t4 = (12, "hell", (1, 2, 4))
print(type(t4[2]))
t5 = 1
print(type(t5))  # type will be given as int instead of tuple
# To create tuple with single element a comma(,) is compulsory
t6 = (1,)
print(type(t6))

t7 = "Prakhar", "Singhal"  # tuple is assumed by default
print(t7)
print(type(t7))

print(t1[::-1])

tpl = (1, 3, 4, 5, [6, 7, 8, 9])
print(tpl[-1][-1])
tpl1 = (1, 2, 2, "upflairs", 2, "upflairs")
# print(max(tpl1))
# print(sum(tpl1))
# print(min(tpl1))
a, b, c, d, e, f = tpl1  # Gives the value of tuple elements to a,b,c.. respectively
print(c)
print(tpl1.count("upflairs"))  # returns the numbers of 'upflairs' in the tuple
print(tpl1.index("upflairs"))  # returns the index of first occurance in the tuple
