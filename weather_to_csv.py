import sqlite3
from WeatherURLClass import WeatherURL
from weather_sql_db import init_db, write_to_db
import os

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

    os.makedirs("data", exist_ok=True)

    weather_data = WeatherURL(url, params)

    json_data = weather_data.get_response_data()

    # Storing raw json data in separate file
    weather_data.raw_json_data(json_data, "data/raw_victoria_hourly_weather.json")

    # Saving json data as a pandas DataFrame
    df = weather_data.to_dataframe(json_data)

    # Storing data in csv file
    weather_data.to_csv(df, "data/victoria_hourly_weather.csv")

    conn = sqlite3.connect("data/hourly_weather.db")
    init_db(conn)

    location = f"{params['latitude']},{params['longitude']}"
    write_to_db(df, conn, location)

    conn.close()


if __name__ == "__main__":
    main()