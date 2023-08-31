print('Question 1')
fish_size = float(input('Size of zander(cm): '))
if fish_size < 42:
    difference = 42 - fish_size
    print(f'Zander size is {difference}cm below the size limit, release the fish')
else:
    print(f'Zander is good ')

print('Question 2')
cabin_class = input("Enter the cabin class of a cruise ship: ")
if cabin_class == 'LUX':
    print('upper-deck cabin with a balcony')
elif cabin_class == 'A':
    print('above the car deck, equipped with a window')
elif cabin_class == 'B':
    print('windowless cabin above the car deck')
elif cabin_class == 'C':
    print('windowless cabin below the car deck')
else:
    print('Invalid cabin class')


print('Question 3')
gender = input('Enter your gender(male/female): ')
hemoglobin_value = float(input('Enter your hemoglobin value (g/l): '))
if gender == 'female':
    if hemoglobin_value < 117:
        print('Your hemoglobin value is low')
    elif 117 <= hemoglobin_value <= 155:
        print('Your hemoglobin value is normal')
    elif hemoglobin_value > 155:
        print('Your hemoglobin value is high')
    else:
        print('invalid input')
elif gender == 'male':
    if hemoglobin_value < 134:
        print('Your hemoglobin value is low')
    elif 134 <= hemoglobin_value <= 167:
        print('Your hemoglobin value is normal')
    elif hemoglobin_value > 167:
        print('Your hemoglobin value is high')
    else:
        print('invalid input')
else:
    print('Invalid gender')

print('Question 4')
year = int(input('Enter a year: '))
if year % 100 == 0 and year % 400 == 0:
    print('It is a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print('It is a leap year')
else:
    print('It is not a leap year')
