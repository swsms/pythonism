letters = ['A', 'B', 'C', 'D', 'E', 'F']
sublist = letters[1:5]
print(sublist)  # ['B', 'C', 'D', 'E']

# the indexes are optional
print(letters[2:])   # ['C', 'D', 'E', 'F']
print(letters[:4])   # ['A', 'B', 'C', 'D']
print(letters[:])    # The full copy: ['A', 'B', 'C', 'D', 'E', 'F']

all_letters = letters[:3] + letters[3:]
print(all_letters)  # The same list: ['A', 'B', 'C', 'D', 'E', 'F']

# customizing step
print(letters[1:5:2])  # ['B', 'D']
print(letters[::2])    # ['A', 'C', 'E']
print(letters[::-1])   # Reversed: ['F', 'E', 'D', 'C', 'B', 'A']

# negative indexes
print(letters[-5:-1])   # ['B', 'C', 'D', 'E']
print(letters[-2:])     # ['E', 'F']
print(letters[:-4])     # ['A', 'B']
print(letters[-1::-1])  # Reversed: ['F', 'E', 'D', 'C', 'B', 'A']

# to be noted
print(letters[5:1])       # Empty list: []
print(letters[5:1:-1])    # ['F', 'E', 'D', 'C']
print(letters[-5:-1:-1])  # Empty list: []
print(letters[-5:-1:1])   # ['B', 'C', 'D', 'E']
