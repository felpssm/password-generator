import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "abcdefghijklmnopqrstuvwxyz".upper()
numbers = "0123456789"
symbols = "!@#$%¨&*()_+=?/<>[]~^.,;:"

all_chars = lower + upper + numbers + symbols
lenght = int(input("Enter a length for 1 to 87 : "))

password = ''.join(random.sample(all_chars, lenght))
print("Generated Password:", password)
