word = 'representative'
substring = word[5:9]
print(substring)  # sent

# the indexes are optional
print(word[2:])  # presentative
print(word[:9])  # represent
print(word[:])   # representative

# customizing step
print(word[2:9:3])  # pst
print(word[::2])    # rpeettv
print(word[::-1])   # Reversed: evitatneserper

# negative indexes
print(word[-12:-5])   # present
print(word[-6:])      # tative
print(word[:-5])      # represent
