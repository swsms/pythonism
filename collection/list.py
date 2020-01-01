empty_list = []  # or list()
print(empty_list)  # []

list_of_things = ['cat', 'robot', ['apple', 'cherry'], 42]
print(len(list_of_things))  # 4
print(list_of_things)  # ['cat', 'robot', ['apple', 'cherry'], 42]

languages = ['English', 'Germany', 'French']
print(languages)  # ['English', 'Germany', 'French']

print(languages[0])   # English
print(languages[-1])  # French
print(languages.index('Germany'))  # 1

languages.append('Hindi')
languages.remove('Germany')
print(languages)  # ['English', 'French', 'Hindi']

languages.insert(1, 'Dutch')
print(languages)  # ['English', 'Dutch', 'French', 'Hindi']

languages.pop(1)
print(languages)  # ['English', 'French', 'Hindi']

languages += ['Portuguese', 'Latin']  # languages.extend(...)
print(languages)  # ['English', 'French', 'Hindi', 'Portuguese', 'Latin']

languages.reverse()
print(languages)  # ['Latin', 'Portuguese', 'Hindi', 'French', 'English']

languages.sort()
print(languages)  # ['English', 'French', 'Hindi', 'Latin', 'Portuguese']

some_languages = languages[1:3]
print(some_languages)  # ['French', 'Hindi']

some_languages *= 2
print(some_languages)  # ['French', 'Hindi', 'French', 'Hindi'
print(some_languages.count('Hindi'))  # 2

some_languages.clear()
print(some_languages)  # []
