
print('Question 1')
num = 0
while num <= 1000:
    if num % 3 == 0:
        print(f'The num {num} is divisible to three')
    num = num + 1
print("That's it")



print('Question 2')
inches = float(input('Enter a length in inches: '))
while inches >= 0:
    cm = inches * 2.54
    print(cm)
    inches = float(input('Enter a length in inches: '))

print("You entered negative value")


print('Question 3')

list_num = []


while True:
    number = input('Enter a no: ')
    if number == '':
        break
    try:
        num_int = int(number)
        list_num.append(num_int)
    except:
        print('Enter a integer')
smallest = min(list_num)
largest = max(list_num)
print(f'Smallest: {smallest}\nLargest: {largest}')

print('Question 4')
import random
guess = int(input('Guess the no: '))
computer = random.randint(1,10)
while guess != computer:
    if guess< computer:
        print('Too low')
    else:
        print('Too high')
    guess = int(input('Guess the no: '))
print('Correct')


print('Question 5')
username = input('Username: ')
password = input('Password: ')
correct_username = 'python'
correct_password = 'rules'
count = 1
while count < 5:
    if username != correct_username or password != correct_password:
        if count < 5:
            username = input('Username: ')
            password = input('Password: ')
            print('')
            count = count + 1

    elif username == correct_username and password == correct_password:
        print('Welcome')
        break
else:
    print('Access denied!')
"""
print('Question 6')
import random
N = int(input('Enter a random points which you want to create: '))
count = 0
n = 0

while count < N:
    x = random.uniform(-1 ,1)
    y = random.uniform(-1 ,1)

    if x**2 + y**2 < 1:
        n += 1
    count += 1

pi = 4 * n / N
print(f"Estimated pi value is: {pi}")


"""















