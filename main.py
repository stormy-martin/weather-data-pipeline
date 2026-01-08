# C3. Import libraries and the WeatherInfo class to creat an instance and call the methods from C2.

from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from weather import WeatherInfo
import sqlite3
from tabulate import tabulate

# Define the chosen location (Amarillo, TX) and date (September 20).
latitude = 35.222
longitude = -101.8313
month = 9  # September
day = 20
years = [2021, 2022, 2023, 2024, 2025]

# Creating an instance of the WeatherInfo class.
weather = WeatherInfo(latitude=latitude, longitude=longitude, month=month, day=day, years=years)
yearly_weather_data = weather.pull_weather_data()

base = declarative_base()

# C4. Create a second class that defines a SQLite table using SQLAlchemy ORM.
# This table includes fields for all required instance variables and weather statistics.
class WeatherEntry(base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    years = Column(Integer, nullable=False)

    # Weather data fields.
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    precipitation_sum = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)


# C4a. Create the SQLite engine and initialized the table.
engine = create_engine('sqlite:///weather_data.db')
base.metadata.drop_all(engine)  # Drop table if it exists for a clean start.
base.metadata.create_all(engine)

# C5. Populate the table created in part C4 with the weather data for your chosen location and date.
Session = sessionmaker(bind=engine)
session = Session()

for year_data in yearly_weather_data:
    record = WeatherEntry(
        latitude=latitude,
        longitude=longitude,
        month=month,
        day=day,
        years=year_data['year'],
        avg_temp=year_data['mean_temperature'],
        min_temp=year_data['mean_temperature'],
        max_temp=year_data['mean_temperature'],
        avg_wind_speed=year_data['max_wind_speed'],
        min_wind_speed=year_data['max_wind_speed'],
        max_wind_speed=year_data['max_wind_speed'],
        precipitation_sum=year_data['precipitation_sum'],
        min_precipitation=year_data['precipitation_sum'],
        max_precipitation=year_data['precipitation_sum']
    )
    session.add(record)

session.commit()
session.close()
print("")
print("Weather data inserted into the database.")

# C6. Write a method that queries the SQLite table and retrieves the data.

def display_weather_records(latitude, longitude, month, day):
    # Connect to SQLite database.
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()

    # SQL query to retrieve the data for Amarillo, TX on September 20th.
    query = """
    SELECT * FROM weather_data
    WHERE latitude = ? AND longitude = ?
    AND month = ? AND day = ?
    ORDER BY years ASC;
    """

    cursor.execute(query, (latitude, longitude, month, day))
    rows = cursor.fetchall()

    # Defining headers for output formatting.

    if rows:
        headers = ["Month", "Day", "Year", "Avg Temp (°F)", "Min Temp (°F)", "Max Temp (°F)", "Avg Wind Speed (mph)",
                   "Min Wind Speed (mph)", "Max Wind Speed (mph)", "Precipitation (inches)"
                   ]

        # Format rows into a table for display
        table_data = []
        for row in rows:
            table_data.append([
                row[3],  # Month
                row[4],  # Day
                row[5],  # Year
                row[6],  # Avg Temp
                row[7],  # Min Temp
                row[8],  # Max Temp
                row[9],  # Avg Wind Speed
                row[10],  # Min Wind Speed
                row[11],  # Max Wind Speed
                row[12]  # Precipitation
            ])

        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    else:
        print("No data found for the specified location and date.")

    cursor.close()
    connection.close()

display_weather_records(latitude, longitude, month, day)

#C6a. Included date and timestamp for report screenshot.
from datetime import datetime
print("Current date and time:", datetime.now())
