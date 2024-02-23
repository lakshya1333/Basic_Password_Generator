import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator created by LJ!!!!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ask = input("What type of password do you need? easy or hard: \n")


if ask == "easy":
  password = ""   
  for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
  for sym in range(1,nr_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym
  for num in range(1,nr_numbers):
    random_num = random.choice(numbers)
    password += random_num
  print(f"Your password is {password}")

elif ask == "hard":
  password_list = []  
  for char in range(1,nr_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char
  for sym in range(1,nr_symbols + 1):
    random_sym = random.choice(symbols)
    password_list += random_sym
  for num in range(1,nr_numbers):
    random_num = random.choice(numbers)
    password_list += random_num
  random.shuffle(password_list)
  pass_hard = ""
  for char in password_list:
    pass_hard += char
  print(f"Your password is {pass_hard}")



  

