
print('Question 1')
seasons = ('Spring', 'Summer', 'Autumn', 'Winter')

month = int(input('Enter a no of a month: '))
if month == 12 or month == 1 or month == 2:
    print(f'It is {seasons[3]}')
elif month == 3 or month == 4 or month == 5:
    print(f'It is {seasons[0]}')
elif month == 6 or month == 7 or month == 8:
    print(f'It is {seasons[1]}')
elif month == 9 or month == 10 or month == 11:
    print(f'It is {seasons[2]}')
else:
    print('Enter a valid no of a month')


print('Question 2')

names = set()

while True:
    add_names = input('Enter a name: ')
    if add_names == '':
        break
    elif add_names in names:
        print('Name exist')
    else:
        names.add(add_names)
        print('New game')

for i in names:
    print(i)


print('Question 3')

airport = {}


def new_airport():
    icao = input('Enter ICAO code: ')
    name = input('Enter name of the airport: ')
    airport[icao] = name

def existing_airport():
    icao = input('Enter ICAO code: ')
    print(airport[icao])


def quit():
    print('Good bye')
    exit()


while True:
    option = input('Enter your option (new/exist/quit): ')
    if option == 'new':
        new_airport()
    elif option == 'exist':
        existing_airport()
    elif option == 'quit':
        quit()
    else:
        print("Invalid option. Please enter new, exist, or quit.")











