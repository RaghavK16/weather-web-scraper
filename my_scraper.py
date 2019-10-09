import pandas as pd
from bs4 import BeautifulSoup
import requests as r

page = r.get('https://forecast.weather.gov/MapClick.php?lat=34.0998&lon=-118.3272#.XZy3dkYzbIU')
# change the fetched link according to the area searched on the site

soup = BeautifulSoup(page.content, 'html.parser')  # gets the entire html code
week = soup.find(id="seven-day-forecast-body")  # gets the week template
items = (week.find_all(class_="tombstone-container"))  # gets the internal items of weeks

period_names = [item.find(class_='period-name').get_text() for item in items]  # list of period names in items
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]  # list of descriptions in items
temperatures = [item.find(class_='temp').get_text() for item in items]  # list of temps in items

weather_info = pd.DataFrame(

    {
        'Day': period_names,
        'Weather': short_descriptions,           # Framing of data into table
        'Temperature': temperatures
    }
)

print(weather_info)

weather_info.to_csv('weather.csv')  # save as .csv file
