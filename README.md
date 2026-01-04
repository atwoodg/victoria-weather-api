# Victoria Weather Analytics

## Overview
A small data analytics project that pulls hourly weather data from the Open-Meteo API and transforms it into a CSV file to be used in Power BI dashboard for reporting. Location can be changed by adjusting parameters.

## Features
- Extracts hourly weather data from Open-Meteo API for Victoria B.C.
- Stores raw data as JSON for debugging.
- Transforms 'hourly' JSON dictionary into pandas DataFrame.
- Ensures dates and times are in proper format for output.
- Loads cleaned result into a CSV file.
- Dashboard connected to CSV output is built in Power BI.

## Tech stack
- Python 3.9.23
  - 'requests' for API calls
  - 'pandas' for data transformation
- Power BI

## Installation
Clone the repo and compile:

```bash
git clone https://github.com/atwoodg/victoria-weather-api

cd victoria-weather-api

#Windows:
.\.venv\Scripts\activate

#macOS/Linux:
source .venv/bin/activate

pip install requests pandas
```

## How to use
Running the system:
```bash
python3 weather_to_csv.py
```
Output will be:
- Raw JSON data
- CSV data

## Credits
- Contributors: Gabriel Atwood
- Sources: https://api.open-meteo.com/v1/forecast?latitude=48.428333&longitude=-123.364722&hourly=temperature_2m,precipitation,wind_speed_10m&timezone=America/Vancouver

