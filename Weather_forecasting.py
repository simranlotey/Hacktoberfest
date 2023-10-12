import requests

def get_weather_forecast(city):
    api_key = "API_KEY"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(base_url, params={"q": city, "appid": api_key})
        response.raise_for_status()
        weather_data = response.json()
        
        # Use Copilot suggestion for extracting temperature, humidity, and wind speed.
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
       
        # Print the weather forecast
        print(f"Weather Forecast for {city}:")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as err:
        # Use Copilot suggestion for error handling
        print(f"Error fetching weather data: {err}")

# Get city name from user as input
city_name = input("Enter the city name: ")

# Call the function to retrieve and display the weather forecast
get_weather_forecast(city_name)



    





























































