import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator!")
length = int(input("How many characters would you like in your password?\n"))
nr_letters = int(input("How many letters would you like?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

while len(password) < length:
    password.append(random.choice(letters + numbers + symbols))

random.shuffle(password)
final_password = ''.join(password)
print(final_password)
