numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = filter(lambda n: n % 2 == 0, numbers)

print(type(even_numbers))  # <class 'filter'>
print(list(even_numbers))  # [0, 2, 8, 34]

persons = [
    ('John', 17),
    ('Cedric', 34),
    ('Penny', 25),
    ('Paul', 16)
]

adult_persons = list(filter(lambda person: person[1] >= 18, persons))
print(adult_persons)  # [('Cedric', 34), ('Penny', 25)]
