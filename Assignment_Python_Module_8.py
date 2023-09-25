"""
print('Question 01')
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='metropolia',
    autocommit=True
)

def icoa_code(icoa):
    sql = 'SELECT ident, name, municipality FROM airport'
    sql += ' WHERE id ="'+ icoa + '"'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        for row in result:
            print(f'Hello! Airport code is {row[0]}. Airport name : {row[1]}. Location: {row[2]}')
    return

icoa = input('Enter ICOA:')
icoa_code(icoa)


print('Question 2')

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='metropolia',
    autocommit=True
)

def icoa_code(icoa):
    sql = 'SELECT name, type FROM airport'
    sql += ' WHERE iso_country ="'+ icoa + '"' + 'ORDER by type'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        for row in result:
            print(f'Hello! Airport name is {row[0]}. Airport name : {row[1]}')
    return

icoa = input('Enter ICOA:')
icoa_code(icoa)



"""
print('Question 03')

import mysql.connector
from geopy.distance import geodesic

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='metropolia',
    autocommit=True
)


def get_airport_coordinates(icao):
    cursor = connection.cursor()
    sql = 'SELECT latitude_deg, longitude_deg FROM airport '
    sql += ' WHERE id = %s'
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    cursor.close()
    lantitude = float(result[0])
    longitude = float(result[1])
    return lantitude, longitude


def calculate_distance(icao1, icao2):
    coord1 = get_airport_coordinates(icao1)
    coord2 = get_airport_coordinates(icao2)

    if coord1 and coord2:
        distance = geodesic(coord1, coord2).kilometers
        return distance
    else:
        return None



icao_code_1 = input('Enter ICAO code 1: ')
icao_code_2 = input('Enter ICAO code 2: ')

distance = calculate_distance(icao_code_1, icao_code_2)

if distance is not None:
    print(f'The distance between {icao_code_1} and {icao_code_2} is approximately {distance:.2f} kilometers.')
else:
    print('One or both of the airports were not found in the database.')

