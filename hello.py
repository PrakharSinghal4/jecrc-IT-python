print(100)
print("Hello")
print('Hey there!')
print(23+100)
# This is a comment
x=3
print(x)
y = 3.3
print(y)
z = "Hello"
print(z)
print(type(x))
print(type(y))
print(type(z))
sum = x + y
print(sum)
print(id(z))

# STRING
st1 = "Hello World"
st2 = "Hello"
print(len(st1))
print("Hello" in st1)
print(st1.lower())
print(st1[0:7])
print(st1[0:7:2])
print(st1[-1:-3]) # NO OUTPUT
print(st1[-1:-3:-1])
print(st1[:]) #print full string (goes from 0 to end by default)
print(st1[::1]) #print full string (goes from 0 to end by default)
print(st1[::-1]) #print full string in reverse (goes from end to start if -1 is mentioned)



# SLICING
print(st1[3])   # 3rd index (l)
print(st1[0:3]) # range (last index is not printed)
print(st1[:3])  # automatically starts from 0
print(st1[0:])  # automatically ends at the last index
print(st2 in st1) # true
print(st2[-1])  # (o)
print(st2[-2:]) # (lo)
# print(st2[5:2]) wrong output





