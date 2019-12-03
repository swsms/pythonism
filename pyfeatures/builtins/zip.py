numbers = [1, 2, 3]
letters = ['C', 'B', 'C']

print(list(zip(numbers, letters)))  # [(1, 'C'), (2, 'B'), (3, 'C')]

names = ['Cedric', 'Penny', 'Kenneth']
ages = [34, 25, 27]
genders = ['M', 'F', 'M']

persons = list(zip(names, ages, genders))

# [('Cedric', 34, 'M'), ('Penny', 25, 'F'), ('Kenneth', 37, 'M')]
print(persons)

letters_to_numbers = {
    'A': 1,
    'B': 2,
    'C': 3
}

inverted_dict = dict(zip(letters_to_numbers.values(),
                         letters_to_numbers.keys()))

print(inverted_dict)  # {1: 'A', 2: 'B', 3: 'C'}
