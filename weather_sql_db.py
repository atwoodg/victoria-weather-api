import sqlite3
import pandas as pd

'''Create required database tables'''
def init_db(conn: sqlite3.Connection):
    curs = conn.cursor()

    curs.execute('''CREATE TABLE IF NOT EXISTS hourly_weather(
                        location,
                        time,
                        temperature_2m,
                        precipitation,
                        wind_speed_10m,
                        date,
                        PRIMARY KEY (location, time))''')

    conn.commit()

'''Load hourly weather data into SQLite for given location'''
def write_to_db(df: pd.DataFrame, conn: sqlite3.Connection, location: str):
    curs = conn.cursor()

    df_copy = df.copy()
    df_copy['location'] = location

    df_copy['time'] = df_copy['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df_copy['date'] = df_copy['time'].str[:10]

    cols = ['location', 'time', 'temperature_2m', 'precipitation', 'wind_speed_10m', 'date']
    rows = list(df_copy[cols].values)

    curs.execute('''DELETE FROM hourly_weather WHERE location = ?''', (location,))

    curs.executemany('''INSERT INTO hourly_weather(location, time, temperature_2m, precipitation, wind_speed_10m, date) 
                            VALUES (?,?,?,?,?,?)''', rows)

    conn.commit()