import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+']

print("Welcome to the Password Generator!")

n_letters = int(input("How many letters do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))

password_list = []

for _ in range(n_letters):
    password_list += random.choice(letters)

for _ in range(n_numbers):
    password_list += random.choice(numbers)

for _ in range(n_symbols):
    password_list += random.choice(symbols)
    
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your generated password is: {password}")
