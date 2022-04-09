import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letters_input = int(input())
print("How many symbols would you like?")
symbols_input = int(input())
print("How many numbers would you like?")
numbers_input = int(input())

random_letters = random.choices(letters, k = letters_input)
random_symbols = random.choices(symbols, k = symbols_input)
random_numbers = random.choices(numbers, k = numbers_input)

password = random_letters + random_numbers + random_symbols

random.shuffle(password)

shuffled_password = "".join(password)

print(f"Your password: {shuffled_password}")
