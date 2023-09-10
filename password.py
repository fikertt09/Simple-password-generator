import random


lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
numbers ="0123456789"
special_symbols = "()[]{} ,;:.-\\?+*&%$#@"


upper, lower, digits, special = True, True, True, True


passlen = int(input("Enter your desirable length of password: "))


all =""

if upper:
    all+= uppercase_letters

if lower:
    all+=lowercase_letters
if digits:
    all+=numbers
if special:
    all+=special_symbols


amount = int(input("How many passwords do you need: "))

for i in range(amount):
    password = "".join(random.sample(all, passlen))
    print(password)


