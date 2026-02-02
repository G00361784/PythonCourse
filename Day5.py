scores =[10,12,13,14,15,16,17,18,19,20]
#sum = 0
max_score = 0
for score in scores:
    if score > max_score:
        max_score = score

print(max_score)

#Range function
sum = 0
for i in range(1,101):
   sum += i
print(sum)

#Password Generator
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+'

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = ''
password_symbols = ''
password_numbers = ''
if nr_letters > 0:
    for char in range(1, nr_letters + 1):
        password_letters += random.choice(letters)
if nr_symbols > 0:
    for char in range(1, nr_symbols + 1):
        password_symbols += random.choice(symbols)
if nr_numbers > 0:
    for char in range(1, nr_numbers + 1):
        password_numbers += random.choice(numbers)
password = password_letters + password_symbols + password_numbers

print(password)


#Order of characters randomised:
password_list = []

for char in password:
    password_list.append(char)


final_password = random.shuffle(password_list)
final_password = ''.join(password_list)

print(final_password)