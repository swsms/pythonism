print('Hello!')  # Hello!

print('Bonjour', 'Privet', 'Konnichiwa')  # Bonjour Privet Konnichiwa
print('Bonjour', 'Privet', 'Konnichiwa', sep=',')  # Bonjour,Privet,Konnichiwa

greetings = ['Bonjour', 'Privet', 'Konnichiwa']
print(greetings)  # ['Bonjour', 'Privet', 'Konnichiwa']

# Bonjour,Privet,Konnichiwa
print('Bonjour', end=',')
print('Privet', end=',')
print('Konnichiwa', end='\n')
