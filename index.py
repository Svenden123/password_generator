import random

letters = ['a', 'b' ,'c', 'd', 'r', 'u', 'p', 'q', 'A', 'B', 'Z', 'Q', 'P', 'Z', 'R']

numbers = ['0', '1', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '%', '*', '(', ')', '&', '_']

print("Welcome")

nr_letters = int(input(f"How many letters do you want in the password ?\n"))
nr_symbols = int(input(f"How many symbols do you want in the password ?\n"))
nr_numbers = int(input(f"How many numbers do you want in the password ?\n"))

password_list = []

for char in range(1, nr_letters+1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

    print(password_list)
