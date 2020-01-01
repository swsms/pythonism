sequence_of_numbers = [x for x in range(5)]
print(sequence_of_numbers)  # [0, 1, 2, 3, 4]

numbers = [1, 2, 3, 5, 8, 13]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)  # [1, 4, 9, 25, 64, 169]

list_of_words = ['right', 'practice', 'awesome', 'creative']
first_upper_letters = [word[0].upper() for word in list_of_words]
print(first_upper_letters)  # ['R', 'P', 'A', 'C']
