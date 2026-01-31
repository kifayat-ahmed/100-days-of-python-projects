# Day 5
# Password generator
import random

letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&']


print("Welcome to the password generator!")
nr_letters = int(input("How many letters would u like on your password?\n"))

nr_symbols = int(input("How many symbols would u like in ur password?\n"))

nr_numbers = int(input("How many numbers would u like in ur password?\n"))

password = ""

for char in range(1, nr_letters +1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, nr_numbers +1):
    random_num = random.choice(numbers)
    password += random_num

for char in range(1, nr_symbols +1):
    random_sym = random.choice(symbols)
    password += random_sym



lst = list(password)
random.shuffle(lst)
password =''.join(lst)

print(password)

