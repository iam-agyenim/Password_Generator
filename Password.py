import random

Letters = ["a" , "b" , "c", "d", "e" , "f", "g" , "i" , "j" , "k" , "L" , "m" "n", "o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#", "$","%","^","&","*","(",")"]

Intro = print("Password Generator\n")
n_letters=int(input("Enter the number of letters you want: "))
n_numbers= int(input("Enter the number of Numbers you want: "))
n_symbols= int(input("Enter the numbe rof symbols you want: "))

password = []
for char in range(1, n_letters+1):
    password += random.choice(Letters)
for char in range(1, n_numbers+1):
    password += random.choice(numbers)
for char in range(1, n_symbols+1):
    password += random.choice(symbols)

random.shuffle(password)
print(f"{''.join(password)}")

