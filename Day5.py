import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
qr_letters = int(input("How many letters would you like in your password?\n"))
qr_symbols = int(input(f"How many symbols would you like?\n"))
qr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for text in range(0, qr_letters):
    password_list.append(random.choice(letters))

for text in range(0, qr_symbols):
    password_list.append(random.choice(symbols))

for text in range(0, qr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for text in password_list:
    password += text

print(f"Your password is: {password}")
