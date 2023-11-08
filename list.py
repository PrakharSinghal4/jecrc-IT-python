# LIST


t2 = (1,'hello',11,12,4,5,5,5)
c1 = [1,2,3.3,"Hello",7.8]
c2 = [0,"Hey",7.8]
type(c1) #list
type(c2) #list
print(c1[0:4])
c2.append(29)
print(c2) # List is mutable
c2.insert(1,666) # add 666 at 1st index
print(c2)
c2.append(t2) # append a tuple to a list
print(c2)
t4 = (c1[3],t2[3])
print(t4)
print(str(c1[3]) + " " +str(t2[3])+ " " +str(c2[3]))


lst = [1,'hello',2.5,1,'c']
lst.pop()
print(lst)
lst.append('c')
print(lst)
lst2 = lst.copy() #copy lst to lst2
print(lst2)
lst.insert(1,'d')
print(lst)
lst.insert(-1,'upflairs')
print(lst)
lst.insert(225,'4.5') # If there is no such index, element will be added at the end of the list
name = 'upflairs'
print(name + '2')
print(name * 2)


