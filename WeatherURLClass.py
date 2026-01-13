import requests
import pandas as pd
import json

class WeatherURL:

    def __init__(self, url: str, params: dict):
        self.url = url
        self.params = params

    '''Call the weather API and return JSON response'''
    def get_response_data(self):

        try:
            # Tries to get server response of data, timeout of 10 seconds to ensure no hanging
            response = requests.get(url=self.url, params=self.params, timeout=10)
            response.raise_for_status()

            if response.json is None:
                raise RuntimeError("API response is empty")
            else:
                return response.json()

        except requests.exceptions.Timeout as e:
            print("Request timed out", e)
            return None

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None

    '''Write the raw API JSON response to data for traceability'''
    def raw_json_data(self, data: dict, path: str):
        try:
            # Storing json data
            with open(path, "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            print(e)

    '''Convert the API JSON response into cleaned pandas dataframe'''
    def to_dataframe(self, data: dict):
        hourly_df = pd.DataFrame(data.get("hourly"))

        if hourly_df.empty:
            raise RuntimeError("Hourly data is empty")

        hourly_df["time"] = pd.to_datetime(hourly_df["time"])
        hourly_df["date"] = hourly_df["time"].dt.date

        return hourly_df

    '''Export the hourly dataframe to a CSV file for POWER BI reporting'''
    def to_csv(self, df: pd.DataFrame , path: str):

        # Convert Data Frame to csv
        df.to_csv(path, index=False)
        return df
