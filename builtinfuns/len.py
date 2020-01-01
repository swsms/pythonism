fruits = ['apple', 'banana', 'cherry']

print(len(fruits))   # 3
print(len('apple'))  # 5

print(len(list()))     # 0
print(len(range(10)))  # 10

job = {
    'title': 'Python Backend Developer',
    'skills': ['Python', 'Django', 'PostgreSQL', 'Git'],
    'salary': '4000 EUR',
}

print(len(job))  # 3
print(len(job['skills']))  # 4
