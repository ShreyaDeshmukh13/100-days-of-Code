print("Welcome to Python Pizza Deliveries!")
size = input("What Size Pizza Do You Want ? S , M , or L :")
pepperoni = input(" Do you want Pepperoni on your pizza ? Y or N :")
extra_cheese = input(" Do you want extra cheese ? Y or N :")

total = 0
if size == 'S':
    total = total + 150
elif size == 'M':
    total = total + 200
else :
    total = total + 250

if pepperoni == 'Y' :
    if size == 'S':
        total = total + 20
    else:
        total = total + 30

if extra_cheese == 'Y':
    total = total + 10

print(f'Your Final bill is Rs:{total}')