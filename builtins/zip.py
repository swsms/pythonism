numbers = [1, 2, 3]
letters = ['A', 'B', 'C']

print(list(zip(numbers, letters)))  # [(1, 'A'), (2, 'B'), (3, 'C')]

numbers = [4, 5, 6]
letters = ['D', 'E', 'F', 'G', 'H']

print(list(zip(numbers, letters)))  # [(4, 'D'), (5, 'E'), (6, 'F')]

names = ['Cedric', 'Penny', 'Kenneth']
ages = [34, 25, 27]
genders = ['M', 'F', 'M']

persons = list(zip(names, ages, genders))

# [('Cedric', 34, 'M'), ('Penny', 25, 'F'), ('Kenneth', 37, 'M')]
print(persons)

letters_to_numbers_dict = {
    'A': 1,
    'B': 2,
    'C': 3
}

inverted_dict = dict(zip(letters_to_numbers_dict.values(),
                         letters_to_numbers_dict.keys()))

print(inverted_dict)  # {1: 'A', 2: 'B', 3: 'C'}
