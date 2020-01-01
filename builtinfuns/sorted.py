numbers = [0, 2, 9, 4, 5, 6, 3, 4, 8]

print(sorted(numbers))  # [0, 2, 3, 4, 4, 5, 6, 8, 9]
print(sorted(numbers, reverse=True))  # [9, 8, 6, 5, 4, 4, 3, 2, 0]

strings = ['a', 'A', 'aa', 'C', 'c', 'AAA']

print(sorted(strings))  # ['A', 'AAA', 'C', 'a', 'aa', 'c']
print(sorted(strings, key=lambda s: len(s)))  # ['a', 'A', 'C', 'c', 'aa', 'AAA']
