numbers = [1, 2, 4, 8, 16, 32]
squares = map(lambda n: n ** 2, numbers)

print(type(squares))  # <class 'map'>
print(list(squares))  # [1, 4, 16, 64, 256, 1024]

names = ['johN', 'ANNA', 'kaTy']
names = list(map(lambda name: name[0].upper() + name[1:].lower(), names))
print(names)  # ['John', 'Anna', 'Katy']

bases = [10, 20, 30, 40]
index = [4, 3, 2, 1]

powers = list(map(pow, bases, index))  # n = base ** index
print(powers)  # [10000, 8000, 900, 40]
