import requests

city=(input("Enter city name :"))

api_key = "51bd2905c0d64d5a3bf40704a929efba"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"]

        print("\nWeather Information")
        print("-------------------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather_condition)

    else:
        print("City not found. Please enter a valid city name.")

except:
    print("Unable to fetch weather data. Check your internet or API key.")





    




