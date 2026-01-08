# C1. Create a class with instance variables for the chosen location and date, including latitude, longitude, month,
# day, year, and placeholders for five-year min/max temperature, min/max wind speed and min/max precipitation statistics.
import requests
class WeatherInfo:
    def __init__(self, latitude, longitude, month, day, years):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.years = years

        # Initialize five-year statistics as None.
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None

        self.avg_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None

        self.sum_precipitation = None
        self.min_precipitation = None
        self.max_precipitation = None

# C2. Write a method that uses Weather API to pull data for the most recent five years on the chosen location and
    # date. This method retrieves all required daily variables for each year and stores them.

    def pull_weather_data(self):
        years_data = []
        for year in self.years:
            url = (f"https://archive-api.open-meteo.com/v1/archive?"
                   f"latitude={self.latitude}&longitude={self.longitude}"
                   f"&start_date={year}-{self.month:02d}-{self.day:02d}"
                   f"&end_date={year}-{self.month:02d}-{self.day:02d}"
                   f"&daily=temperature_2m_mean,wind_speed_10m_max,precipitation_sum"
                   f"&temperature_unit=fahrenheit&wind_speed_unit=mph"
                   f"&precipitation_unit=inch&timezone=America/Chicago"
                   )
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # Store daily weather data in a dictionary for each year.
                daily_data = {
                    "year": year,
                    "mean_temperature": data['daily']['temperature_2m_mean'][0],
                    "max_wind_speed": data['daily']['wind_speed_10m_max'][0],
                    "precipitation_sum": data['daily']['precipitation_sum'][0]
                }
                years_data.append(daily_data)
            else:
                print(f"Unable to retrieve data for {year}: {response.status_code}")

        return years_data

    # C2a. Method for mean temperature in Fahrenheit.
    def get_mean_temp(self):
        weather_data = self.pull_weather_data()
        return [(year_data["year"], year_data["mean_temperature"]) for year_data in weather_data]

    # C2b. Method for maximum wind speed in mph.

    def get_max_wind_speed(self):
        weather_data = self.pull_weather_data()
        return [(year_data["year"], year_data["max_wind_speed"]) for year_data in weather_data]

    # C2c. Method for precipitation sum in inches.

    def get_sum_precipitation(self):
        weather_data = self.pull_weather_data()
        return [(year_data["year"], year_data["precipitation_sum"]) for year_data in weather_data]







