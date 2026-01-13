# Victoria Weather Analytics

## Overview
A small data analytics project that pulls hourly weather data from the Open-Meteo API and transforms it into a CSV file to be used in a Power BI dashboard for reporting. Location can be changed by adjusting parameters.

## Features
- Extracts hourly weather data from Open-Meteo API for Victoria, B.C.
- Stores raw data as JSON for debugging.
- Transforms 'hourly' JSON dictionary into pandas DataFrame.
- Ensures dates and times are in proper format for output.
- Loads cleaned result into a CSV file.
- Dashboard connected to CSV output is built in Power BI.
- Also loads the result into a SQLite database for storage.

## Tech stack
- Python 3.9.23
  - 'requests' for API calls
  - 'pandas' for data transformation
- SQLite
- Power BI

## Installation
Clone the repo and compile:

```bash
git clone https://github.com/atwoodg/victoria-weather-api
cd victoria-weather-api

#Windows:
py -m venv .venv
.\.venv\Scripts\activate

#macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate

pip install requests pandas
```

## How to use
Running the system:
```bash
# Run the pipeline to update the CSV:
python weather_to_csv.py
```

Power BI Dashboard:
Home -> Refresh

Files output in \data:
- Raw JSON data
- CSV data

## Credits
- Contributors: Gabriel Atwood
- Sources: https://api.open-meteo.com/v1/forecast?latitude=48.428333&longitude=-123.364722&hourly=temperature_2m,precipitation,wind_speed_10m&timezone=America/Vancouver

