from WeatherURLClass import WeatherURL

def main():

    #Define API
    url = "https://api.open-meteo.com/v1/forecast"

    #Parameters for url
    params = {
        "latitude": 48.428333,
        "longitude": -123.36472,
        "hourly": "temperature_2m,precipitation,wind_speed_10m",
        "timezone": "America/Vancouver"
    }

    weather_data = WeatherURL(url, params)

    # Storing raw json data in separate file
    weather_data.raw_json_data("data/raw_victoria_hourly_weather.json")

    # Storing data in csv file
    weather_data.to_csv("data/victoria_hourly_weather.csv")

if __name__ == "__main__":
    main()