letters = ['A', 'B', 'C', 'D', 'E', 'F']

# getting sublists
print(letters[1:5])  # ['B', 'C', 'D', 'E']
print(letters[2:])   # ['C', 'D', 'E', 'F']
print(letters[:4])   # ['A', 'B', 'C', 'D']
print(letters[:])    # The full copy: ['A', 'B', 'C', 'D', 'E', 'F']

# customizing step
print(letters[1:5:2])  # ['B', 'D']
print(letters[::2])    # ['A', 'C', 'E']
print(letters[::-1])   # Reversed: ['F', 'E', 'D', 'C', 'B', 'A']

# negative indices
print(letters[-5:-1])   # ['B', 'C', 'D', 'E']
print(letters[-2:])     # ['E', 'F']
print(letters[-4:])     # ['C', 'D', 'E', 'F']
print(letters[-1::-1])  # Reversed: ['F', 'E', 'D', 'C', 'B', 'A']

# to be noted
print(letters[5:1])       # Empty list: []
print(letters[5:1:-1])    # Empty list: ['F', 'E', 'D', 'C']
print(letters[-5:-1:-1])  # []
print(letters[-5:-1:1])   # ['B', 'C', 'D', 'E']
