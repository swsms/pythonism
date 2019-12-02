numbers = [0, 2, 9, 4, 5, 6, 3, 4, 8]

print(min(numbers))  # 2
print(max(numbers))  # 9

strings = ['a', 'A', 'b', 'aa', 'C', 'c', 'AAA']

print(min(strings))  # A
print(max(strings))  # c

print(min(strings, key=lambda s: len(s)))  # 'a'
print(max(strings, key=lambda s: len(s)))  # 'AAA'

empty = []
print(min(empty, default=0))  # otherwise, it raises ValueError
