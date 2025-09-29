import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
           'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+','(',')']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input(f"How many symbols would you like?\n"))
nr_number = int(input(f"How many numbers would you like?\n"))

'''Here the password generated is an easier version ,since the letters,symbols 
and numbers are being generated at a fix sequence'''
password = ""
for i in range(1, nr_letters + 1):
    password += random.choice(letters)

for i in range(1, nr_symbol + 1):
    password += random.choice(symbols)

for i in range(1, nr_number + 1):
    password += random.choice(numbers)

print(f'Easy : {password}')

'''Generating an harder password by letters,symbols and numbers being at random positions'''
password_list = []
for i in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for i in range(1, nr_symbol + 1):
    password_list.append(random.choice(symbols))

for i in range(1, nr_number + 1):
    password_list.append(random.choice(numbers))

print(f'Before Shuffling {password_list}')
random.shuffle(password_list)
print(f'After Shuffling{password_list}')

#Converting List back to string
password = ""
for char in password_list:
    password += char

print(f'Harder version of your password is \n{password}')
