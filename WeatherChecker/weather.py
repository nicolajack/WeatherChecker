# to allow to request weather data from api
import requests

# to set api key
API_KEY = '2e687fffa63bdaa4035a52abe653e654'

# to allow users to enter their city
userCity = input("Enter your city: ")

# to create the url for the api request using the user input and api key
url = f'http://api.openweathermap.org/data/2.5/weather?q={userCity}&appid={API_KEY}'

# to get the response from the api
response = requests.get(url)

# to check if the request was successful
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    fTemp = round((((temperature - 273.15) * 1.8) + 32), 2)
    
    print(f'Temperature: {fTemp} °F')
    print(f'Weather Description: {weather_description}')
else:
    print("Error: Unable to fetch weather data. Please check the city name.")