"""
print('Question 1')
import random
i = 1
all_dice = []
total = 0
no = int(input('How many dice: '))
for i in range(1, no+1):
    dice = random.randint(1,6)
    i = i + 1
    all_dice.append(dice)
    total = total + dice
print(all_dice)
print(total)

"""
print('Question 2')

a = []
user = 0
while True:
    user = input('Enter a no: ')
    if user == '':
        break
    try:
        user_int = int(user)
        a.append(user_int)
    except:
        print('Enter an integer')

for elements in a:
    a.sort(reverse=True)
print(a[:5])


"""
try:
    user = 1
    while j < user:
        user = int(input('Enter a no: '))
        j = j + 1
        a.append(user)
except():
    a.sort(reverse=True)
print(a)
"""
"""
print('Question 3')
number = int(input('Enter a number: '))
count = 0
for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print('It is a prime no')
else:
    print('It is not a prime no')


"""
print('Question 4')
city = []
for i in range(5):
    cities = input('Enter a city: ')
    city.append(cities)

for x in range(5):
    print(city[x])


















