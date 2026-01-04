import requests
import pandas as pd
import json

class WeatherURL:

    def __init__(self, url: str, params: dict):
        self.url = url
        self.params = params

    def get_response_data(self):
        try:
            # Tries to get server response of data, timeout of 10 seconds to ensure no hanging
            response = requests.get(url=self.url, params=self.params, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout as e:
            print("Request timed out", e)
            return None

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None

    def raw_json_data(self, path):
        try:
            # Storing json data
            with open(path, "w") as f:
                json.dump(self.get_response_data(), f, indent=4)

        except Exception as e:
            print(e)

    def to_dataframe(self):
        hourly = self.get_response_data().get("hourly")

        if not hourly:
            raise RuntimeError

        df = pd.DataFrame(hourly)
        df["time"] = pd.to_datetime(df["time"])
        df["date"] = df["time"].dt.date

        return df

    def to_csv(self, path):
        df = self.to_dataframe()

        # Convert Data Frame to csv
        df.to_csv(path, index=False)
        return df