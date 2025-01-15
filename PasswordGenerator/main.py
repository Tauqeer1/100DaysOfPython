import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
            'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbol would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_string = ''
shuffled_password_string = ''
for number in range(nr_letters):
    password_string += random.choice(letters)
    
for number in range(nr_symbols):
    password_string += random.choice(symbols)

for number in range(nr_numbers):
    password_string += random.choice(numbers)


shuffled_password_string = ''.join(random.sample(password_string, len(password_string)))

print(password_string)
print(shuffled_password_string)