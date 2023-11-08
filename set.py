#SET
# Immutable
# Heterogenous
# Doesn't allow duplicate elements
# Doesn't maintain the order of data insertion
# {} is used for creating set

set1 = {20,'Prakhar', 3.5, 'c'}
# print(type(set1))
print(set1) #will not print in the same order as inserted (unordered)
# print(set1[0]) -> error 


# set2 = {2,5,6,[4,7,1]}
# print(set2) -> List cannot be inserted in set


set2 = {2,5,6,(4,7,1)}
print(set2) # Tuple CAN be inserted in set


# set3 = {1,2,3,{4,5,6}}
# print(set3) -> Set CANNOT be inserted in a set


set4 = {1,1,3,5,8}
print(set4) # If duplicate elements are inserted in a set it will remove the duplicate elements keeping only one


list1 = [1,1,1,2,2,2,3,3,3,5,5,6]
print(list1)
print(set(list1)) # typecasting list into set

tup1 = (1,1,1,2,2,2,3,3,3,5,5,6)
print(tup1)

print(set(tup1)) # typecasting tuple into set


set5 = {2,9,6,1,5,7,4,6,7,8,'a','c'}
set5.add(9) # adds an element in the set. Behind the scenes a new set with added element is created while the original is destroyed
print(set5) 

set5.remove(9) # removes an element in the set. Behind the scenes a new set with the element removed is created while the original is destroyed
print(set5)

set5.discard(8) # Works similar to remove but doesn't throw error if the element is not found in the set (unlike remove)
print(set5)

set5.pop()
print(set5) # removes a random element from the set

set5.update(set4) # Merges set4 into set5 while removing the duplicate elements
print(set5)

# set5.clear() -> Clears the set
# print(set5)
