"""
print("Question 1")
name = input('Enter your name: ')
print(f'Hello, {name}!')

print('Question 2')
import math
radius = float(input('Enter radius: '))
area = math.pi * radius**2
print(f'Area is: {area}')


print('Question 3')
length = float(input('Enter the length: '))
width = float(input('Enter the width: '))
perimeter = 2 * (length + width)
area_of_rectangle = length * width
print(f'Perimeter: {perimeter} & Area: {area_of_rectangle}')
"""
print('Question 4')
num_1 = int(input('Enter integer 01: '))
num_2 = int(input('Enter integer 02: '))
num_3 = int(input('Enter integer 03: '))
total = num_1 + num_2 + num_3
product = num_1 * num_2 * num_3
average = total/3
print(f'Sum: {total} , Product: {product}, Average: {average:.2f}')

print('Question 5')
talents = float(input('Enter talents: '))
pounds = float(input('Enter pounds: '))
lot = float(input('Enter lots: '))

talents_g = 20 * 32 * 13.3 * talents
pounds_g = 32 * 13.3 * pounds
lot_g = 13.3 * lot

mass = talents_g + pounds_g + lot_g
kg = mass // 1000
kg_int = int(kg)
g = mass % 1000
print(f'The weight in modern units:\n{kg_int} kilograms and {g:.2f} grams')

print('Question 6')
print('3 digit code')
import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
print(f'Your code is: {num1}{num2}{num3}')

print('4 digit code')
num4 = random.randint(1,6)
num5 = random.randint(1,6)
num6 = random.randint(1,6)
num7 = random.randint(1,6)
print(f'Your code is: {num4}{num5}{num6}{num7}')
