fruits = ('apple', 'banana', 'cherry')

print(fruits)     # ('apple', 'banana', 'cherry')
print(fruits[0])  # apple

print(fruits.count('apple'))   # 1
print(fruits.index('cherry'))  # 2

single_item_tuple = ('apple',)
print(type(single_item_tuple))  # <class 'tuple'>

not_a_tuple = ('apple')
print(type(not_a_tuple))  # <class 'str'>

letters1 = 'a', 'b'  # packing
print(letters1)  # ('a', 'b')

a, b = letters1  # unpacking
print(a, b)  # a b

letters2 = ('d', 'e')
print(letters1 + letters2)  # ('a', 'b', 'd', 'e')
