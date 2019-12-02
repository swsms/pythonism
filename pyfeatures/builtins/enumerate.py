seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons)))

# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
print(list(enumerate(seasons, start=1)))

# 1 -> Spring
# 2 -> Summer
# 3 -> Fall
# 4 -> Winter
for number, season in enumerate(seasons, 1):
    print(f'{number} -> {season}')
