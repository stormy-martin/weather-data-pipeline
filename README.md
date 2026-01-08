# Weather Data Pipeline for Event Planning

## Overview
This project was created to demonstrate how historical weather data can be pulled from a public API, stored in a relational database, and queried for basic analysis. The scenario is based on an event planning company that needs to understand historical weather conditions when planning outdoor events.

The program retrieves five years of historical weather data for a specific location and date, including temperature, wind speed, and precipitation, and stores the results in a SQLite database for easy querying.

---

## What This Project Does
- Pulls historical weather data from the Open-Meteo API
- Uses Python classes and methods to organize API logic
- Stores weather data in a SQLite database using SQLAlchemy
- Queries the database and outputs a formatted table for analysis

The focus of this project is on data ingestion, storage, and basic reporting rather than advanced analytics.

---

## Technologies Used
- Python
- Requests (API calls)
- SQLAlchemy (ORM)
- SQLite
- Tabulate (formatted console output)

---

## Project Structure
weather-data-pipeline/
├── README.md
├── requirements.txt
├── weather.py
└── main.py

---

## How the Program Works
1. A location (latitude and longitude) and a specific month and day are defined.
2. The program retrieves historical weather data for that date over the past five years using a public weather API.
3. The data is stored in a SQLite database using SQLAlchemy ORM models.
4. SQL queries retrieve the stored data and display it in a clean, readable table.

---

## How to Run the Project
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the program:
   python main.py

The program will pull the weather data, store it in the database, and print a formatted table of results to the console.

---

## Example Use Case
An event planning team can use this type of analysis to better understand historical weather patterns for a specific date and location. This can help with decisions such as tent sizing, weather coverage, and general event logistics.

---

## Notes
- Weather data is retrieved dynamically from a public API.
- No external datasets are stored in this repository.
- This project was completed as part of the WGU Scripting and Programming Applications course.
