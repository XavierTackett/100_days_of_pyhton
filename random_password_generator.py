#Password Generator Project
import random
import string 
letters = list(string.ascii_letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ----------------------------------------------method 1------------------------------------------------------
password = ""
#Random letters
for char in range(1, nr_letters + 1):
  random_letter = random.choice(letters)
  password += random_letter
#Random symbols
for symbol in range(1, nr_symbols + 1):
  random_sym = random.choice(symbols)
  password += random_sym
#Random numbers
for num in range(1 , nr_numbers + 1):
  random_num = random.choice(numbers)
  password += random_num
#Password shuffle
password = ''.join(random.sample(password,len(password)))
print(f"\nThis is your randomly generated password: {password}")

# ---------------------------------------Method 2 (same results)------------------------------------------------------
password_list = []
#Random letter
for char in range(1, nr_letters + 1):
  random_letter = random.choice(letters)
  password_list += random_letter
#Random symbol 
for symbol in range(1, nr_symbols + 1):
  random_sym = random.choice(symbols)
  password_list += random_sym
#Random number
for num in range(1 , nr_numbers + 1):
  random_num = random.choice(numbers)
  password_list += random_num

random.shuffle(password_list)
password2 = ""

for char in password_list:
  password2 += char
print(f"\nThis is your another randomly generated password: {password2}")
