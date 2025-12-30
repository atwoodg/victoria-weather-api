import requests
import pandas as pd

#Define API
url = "https://api.open-meteo.com/v1/forecast?latitude=48.428333&longitude=-123.364722&hourly=temperature_2m,precipitation,wind_speed_10m&timezone=America/Vancouver"

#GET request
try:
    #Tries to get server response of data, timeout of 10 seconds to ensure no hanging
    response = requests.get(url, timeout=10)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.RequestException as e:
    print("ERROR:", e)

#Save response data as json object
data = response.json()
hourly = data["hourly"]

#Convert hourly data to Data Frame
df = pd.DataFrame(hourly)

#Convert Data Frame to csv
df.to_csv("victoria_hourly_weather.csv", index=False)
