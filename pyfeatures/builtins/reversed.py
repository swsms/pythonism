fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13]

iterator = reversed(fib_numbers)
print(type(iterator))  # <class 'list_reverseiterator'>
print(list(iterator))  # [13, 8, 5, 3, 2, 1, 1, 0]
