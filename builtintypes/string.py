greeting = 'Hello world!'
question = "How are you?"

message = greeting + ' ' + question
print(message)  # Hello world! How are you?
print(len(message))  # 25

print(message.count('H'))  # 2
print(message.find('H'))   # 0
print(message.rfind('H'))  # 13

print(message.upper())  # HELLO WORLD! HOW ARE YOU?
print(message.lower())  # hello world! how are you?
print(message.title())  # Hello World! How Are You?

print(message.capitalize())  # Hello world! how are you?
print(message.casefold())    # hello world! how are you?

print('-'.join(['1', '2', '3']))  # 1-2-3
