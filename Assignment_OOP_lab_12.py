# Question1
import requests

def chuck_norris_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        joke = data['value']
        print("Chuck Norris Joke:")
        print(joke)
    else:
        print("Sorry, there was an unexpected error in fetching a Chuck Norris joke :(")

if _name_ == "_main_":
    chuck_norris_joke()


# Question2
import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15  # Conversion formula from Kelvin to Celsius


def fetch_weather_info(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

        print(f"Weather in {city.capitalize()}:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print("Failed to fetch weather information")



api_key = 'ea56930a92f3b9b3b697c2cb5de262e1'
city = input("Enter the name of a municipality: ")

fetch_weather_info(api_key, city)


