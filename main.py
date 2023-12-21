import requests

def get_weather(city, country):
    api_key = "#PUT YOUR OWN KEY"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": f"{city},{country}", "appid":api_key, "units":"metric"}

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if weather_data["cod"]== "404":
        return "City Not Found!, Please Try Again"

    temperature = weather_data["main"] ["temp"]
    description = weather_data["weather"][0]["description"]

    return f"The temperature in {city}, {country} is {temperature}°C with {description}"

city = input("Enter the city:")
country = input("Enter the country:")
weather_info = get_weather(city, country)

print(weather_info)

