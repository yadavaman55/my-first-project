import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

use_letters = input("Letters (y/n): ").lower()
use_numbers = input("Numbers (y/n): ").lower()
use_symbols = input("Symbols (y/n): ").lower()

characters = ""

if use_letters == 'y':
    characters += string.ascii_letters
if use_numbers == 'y':
    characters += string.digits
if use_symbols == 'y':
    characters += string.punctuation

if characters == "":
    print("You must select at least one character type!")
else:
    password = "".join(random.choice(characters) for i in range(length))
    print("Generated Password:", password)