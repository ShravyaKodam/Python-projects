#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
r_letters = int(input("How many letters would you like in your password?\n"))
r_symbols = int(input(f"How many symbols would you like?\n"))
r_numbers = int(input(f"How many numbers would you like?\n"))
passwordList=[]
for i in range(1,r_letters+1):
    passwordList.append(random.choice(letters))
for i in range(1,r_symbols+1):
    passwordList.append(random.choice(symbols))
for i in range(1,r_numbers+1):
    passwordList.append(random.choice(numbers))
#print(passwordList)
random.shuffle(passwordList)
#print(passwordList)

confidential=""
confidential=confidential.join(passwordList)
print(confidential)