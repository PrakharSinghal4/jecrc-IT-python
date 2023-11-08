# DICTIONARY in python
# Items are stored without index value
# Keys in dictionary must be unique
# Dictionary is mutable


# d1 = {'a':10, 20:50, 3.5:30, 'd': 'Prakhar', 'e': (1,2,3,4), 'f': [5,6,7,8], 'g': {9,10,11,12}}
# print(d1,'\n')
# print(type(d1))
d2 = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50, 'f': 'Prakhar'}
print(d2['a'])
print(d2['f'])
print(d2.keys())
print(d2.values())
d2['a'] = 70
print(d2['a'])

d2.pop('a')  #Requires a key as an argument
print(d2)

# print(d2*2) -> Not allowed

d3 = {'g':60, 'h':70}

d2.update(d3)
print(d2)

# print(d2['ab'])  -> Gives an error if the given key is not found
print(d2.get('ab')) # Returns 'none' (by default)
print(d2.get('ab','NOT FOUND')) # Custom string if the key is not found
