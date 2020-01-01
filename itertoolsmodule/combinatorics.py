import itertools

letters = ['A', 'B', 'C']

letters_numbers = list(itertools.product(letters, [1, 2]))
print(letters_numbers)  # 6
print(letters_numbers)  # [('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)]

permutations = list(itertools.permutations(letters, len(letters)))
print(len(permutations))  # 6
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'),
#  ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
print(permutations)

permutations2 = list(itertools.permutations(letters, 2))
print(len(permutations2))  # 6
# [('A', 'B'), ('A', 'C'), ('B', 'A'),
#  ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(permutations2)

combinations2 = list(itertools.combinations(letters, 2))
print(len(combinations2))  # 3
print(combinations2)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
