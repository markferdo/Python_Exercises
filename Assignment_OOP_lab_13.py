# Question 1
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = {"Number": number, "isPrime": is_prime(number)}
    response_data = json.dumps(result)
    return response_data, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)

# Question 2
from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

@app.route('/airport/<icao>', methods=['GET'])
def airport_info(icao):
    connection = mysql.connector.connect(
        database='flight_game',
        host='127.0.0.1',
        user='mark',
        password='metropolia'
    )
    cursor = connection.cursor()

    query = f"SELECT name, municipality FROM airport WHERE name = %s"
    cursor.execute(query, (icao,))

    airport = cursor.fetchone()

    if airport:
        response_data = {
            "ICAO": icao.upper(),
            "Name": airport_info[0],
            "Location": airport_info[1]
        }
        connection.close()
        response_json = json.dumps(response_data)
        return Response(response_json, status=200, content_type='application/json')

    connection.close()
    return Response(status=404)

if __name__ == '__main__':
    app.run(debug=True)
