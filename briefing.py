#!/bin/python
import urllib.request
from bs4 import BeautifulSoup
import subprocess
import http.client
import requests
import json
import datetime


#Covid-19 Bulgaria tracker
covid_url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

covid_querystring = {"country":"Bulgaria"}

covid_headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "6342ff812bmsh0c48a16910fdd64p1f9c37jsn8ce4bd29dbbe"
    }

covid_response = requests.request("GET", covid_url, headers=covid_headers, params=covid_querystring)
covid_data = json.loads(covid_response.text)

quote_page = 'https://dir.bg'

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Sofia&lang=bg&units=metric&APPID=3a50373a38f976e9ff0d235adeffec15")

weather_data = json.loads(response.text)
#response_traffic = requests.get("https://traffic.ls.hereapi.com/traffic/6.3/incidents.json?apiKey=BibhE_EZKFnQE5z8U6rRitkT_bzo4uSfP_G0SPGxTBk&bbox=42.697,23.324;42.650,23.633&criticality=minor")
#traffic_data = json.loads(response_traffic.text)
#print(traffic_data)

#Bing maps
response_traffic = requests.get("http://dev.virtualearth.net/REST/v1/Traffic/Incidents/42.70,23.33,-42.7,-156.67/severity=2,3,4&type=1,2,10&key=Atz5fm_pJnaBGXBLLnqpz7EATHVKR-iAstXVpeclGg-Phk-bhe99Lh1Llpts_HOf")
#response_traffic = requests.get("http://dev.virtualearth.net/REST/V1/Traffic/Incidents/37,-105,45,-94/true?t=9,2&s=2,3&o=xml&key=Atz5fm_pJnaBGXBLLnqpz7EATHVKR-iAstXVpeclGg-Phk-bhe99Lh1Llpts_HOf")
#traffic_data_bing = json.loads(response_traffic.text)
#print(traffic_data_bing)
#print(response_traffic.text)


#Wind Direction Converter
def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return arr[(val % 16)]



temp = weather_data['main']['temp']

#Wind Speed
wind_speed = weather_data['wind']['speed']

#Description 
description = weather_data['weather'][0]['description']

#Latitude
latitude = weather_data['coord']['lat']

#Longitude 
longitude = weather_data['coord']['lon']

#FeelsLike 
feels_like = weather_data['main']['feels_like']

#Humidity
humidity = weather_data['main']['humidity']

#Pressure
pressure = weather_data['main']['pressure']

#Visibility
visibility = weather_data['visibility']

#Wind Direction
windDir = weather_data['wind']['deg']
wind_dir = degToCompass(windDir)

#Sunrise
sunrise_unix = weather_data['sys']['sunrise']
sunrise = datetime.datetime.fromtimestamp(sunrise_unix).strftime('%H:%M:%S UTC (+3 Sofia)')

#Sunset
sunset_unix = weather_data['sys']['sunset']
sunset = datetime.datetime.fromtimestamp(sunset_unix).strftime('%H:%M:%S UTC (+3 Sofia)')
#Covid Confirmed
covid_conf = covid_data['data']['confirmed']

#Covid Deaths
covid_deaths = covid_data['data']['deaths']

#Covid Recovered
covid_recovered = covid_data['data']['recovered']

# Printing Data
print('\nКоронавирус заразени -> ',covid_conf)
print('\nКоронавирус умрели -> ',covid_deaths)
print('\nКоронавирус излекувани -> ',covid_recovered)
print('\nТемпература -> ',temp)
print('\nУсеща се като -> ',feels_like)
print('\nОписание -> ',description)
print('\nСкорост на вятъра -> ',wind_speed, 'm/s')
print('\nПосока на вятъра -> ', wind_dir)
print('\nВлажност -> ',humidity, '%')
print('\nАтмосферно налягане -> ',pressure, 'hPa')
print('\nВидимост -> ',visibility, 'метра')
print('\nИзгрев -> ',sunrise)
print('\nЗалез -> ',sunset, '\n')



page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
big_img_news = soup.find('div', attrs={'class': 'img-section'})
endText = big_img_news.get_text()
formattedText = endText.replace("\n", " ")

formTxt = formattedText.split()

firstIndex = formTxt.index('|') + 3
formTxt.insert(firstIndex, "\n")
outputNews = " ".join(str(x) for x in formTxt)

print(outputNews)
