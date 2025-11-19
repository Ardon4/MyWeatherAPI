#Import the HTTP library
import requests
API_KEY = "e65642b489ca059510c68f32056bd8c0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
#function to fetch the weather
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

#Handle errors and display data
    if str(data.get("cod")) != "200":
        print("City not found or API error.")
        return
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].title()
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print("\n WEATHER REPORT")
    print(f"City: {city}")
    print(f"Temperature: {temp}C")
    print(f"Condition: {desc}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s\n")

#User loop
while True:
    city = input("Enter city name (or 'exit'): ")
    if city.strip().lower() == "exit":
        break
    get_weather(city.strip())
