import sys
import subprocess
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#def install_libraries():
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'datetime'])
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyQt5'])

#install_libraries()

import datetime as dt 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import requests
import time
import os
from threading import Thread
from datetime import datetime
import random

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api.key', 'r').read()
CITY = "Hamburg"

def kelvin_to_cel(kelvin):
    celsius = kelvin - 273.15
    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_cel(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_cel = kelvin_to_cel(feels_like_kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
desc = response['weather'][0]['description']
print(desc)
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

def weatherimage():
    global weatherimg
    global weatherimg2
    print(desc)
    print(desc2)
    if desc == "overcast clouds":
        weatherimg = "images/e02d.png"
    elif desc == "clear sky":
        weatherimg = "images/e01d.png"
    elif desc == "scattered clouds":
        weatherimg = "images/e03d.png"
    elif desc == "broken clouds":
        weatherimg = "images/e04d.png"
    elif desc == "rain" or "light intensity shower rain" or "heavy intensity shower rain" or "ragged shower rain":
        weatherimg = "images/e10d.png"
    elif desc == "snow" or "freezing rain" or "light snow" or "heavy snow" or "sleet" or "light shower sleet" or "shower sleet" or "light rain and snow" or "rain and snow" or "light shower snow" or "shower snow" or "heavy shower snow":
        weatherimg = "images/e13d.png"
    elif desc == "mist" or "smoke" or "haze" or "sand/dust whirls" or "fog" or "sand" or "dust" or "volcanic ash" or "squalls" or "tornado":
        weatherimg = "images/e50d.png"
    elif desc == "thunderstorm" or "thunderstorm with light rain" or "thunderstorm with rain" or "thunderstorm with heavy rain" or "light thunderstorm" or "heavy thunderstorm" or "ragged thunderstorm" or "thunderstorm with light drizzle" or "thunderstorm with drizzle" or "thunderstorm with heavy drizzle":
        weatherimg = "images/e11d.png"
    elif desc == "shower rain" or "light rain" or "moderate rain" or "heavy intensity rain" or "very heavy rain" or "extreme rain" or "light intensity drizzle" or "drizzle" or "heavy intensity drizzle" or "light intensity drizzle rain" or "drizzle rain" or "heavy intensity drizzle rain" or "shower rain and drizzle" or "heavy shower rain and drizzle" or "shower drizzle":
        weatherimg = "images/e09d.png"
    else:
        weatherimg = "images/X.png"
    
    if desc2 == "overcast clouds":
        weatherimg2 = "images/e02d.png"
    elif desc2 == "clear sky":
        weatherimg2 = "images/e01d.png"
    elif desc2 == "scattered clouds":
        weatherimg2 = "images/e03d.png"
    elif desc2 == "broken clouds":
        weatherimg2 = "images/e04d.png"
    elif desc2 == "rain" or "light intensity shower rain" or "heavy intensity shower rain" or "ragged shower rain":
        weatherimg2 = "images/e10d.png"
    elif desc2 == "snow" or "freezing rain" or "light snow" or "heavy snow" or "sleet" or "light shower sleet" or "shower sleet" or "light rain and snow" or "rain and snow" or "light shower snow" or "shower snow" or "heavy shower snow":
        weatherimg2 = "images/e13d.png"
    elif desc2 == "mist" or "smoke" or "haze" or "sand/dust whirls" or "fog" or "sand" or "dust" or "volcanic ash" or "squalls" or "tornado":
        weatherimg2 = "images/e50d.png"
    elif desc2 == "thunderstorm" or "thunderstorm with light rain" or "thunderstorm with rain" or "thunderstorm with heavy rain" or "light thunderstorm" or "heavy thunderstorm" or "ragged thunderstorm" or "thunderstorm with light drizzle" or "thunderstorm with drizzle" or "thunderstorm with heavy drizzle":
        weatherimg2 = "images/e11d.png"
    elif desc2 == "shower rain" or "light rain" or "moderate rain" or "heavy intensity rain" or "very heavy rain" or "extreme rain" or "light intensity drizzle" or "drizzle" or "heavy intensity drizzle" or "light intensity drizzle rain" or "drizzle rain" or "heavy intensity drizzle rain" or "shower rain and drizzle" or "heavy shower rain and drizzle" or "shower drizzle":
        weatherimg2 = "images/e09d.png"
    else:
        weatherimg2 = "images/X.png"

cities = [
    "Berlin",
    "Frankfurt",
    "Magdeburg",
    "New York",
    "Moscow",
    "London",
    "Yakutsk",
    "Warsaw",
    "Madrid",
    "Barcelona",
    "Sydney"
]

def new_city():
    global city2
    global desc2
    global url2
    global response2
    global temp_kelvin2
    global temp_celsius2
    global country
    city2 = random.choice(cities)
    print(city2)
    url2 = BASE_URL + "appid=" + API_KEY + "&q=" + city2
    response2 = requests.get(url2).json()
    temp_kelvin2 = response2['main']['temp']
    temp_celsius2 = kelvin_to_cel(temp_kelvin2)
    desc2 = response2['weather'][0]['description']
    country = response2['sys']['country']
    time.sleep(5)
    Thread(target = new_city).start()


class MainWindow(QWidget):

    def __init__(self):
        global weatherimg
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 1280, 720) 
        # creating a label widget 
        self.label_3 = QLabel(self) 
  
        # moving position 
        self.label_3.move(0, 0) 
  
        # setting up the border and adding image to background 
        self.label_3.setStyleSheet("background-image : url(bg.jpg); border : 4px solid white") 
        # setting label text 
        self.label_3.resize(1280, 720)
        
        self.label_1 = QLabel(f"Temperature in {CITY}: {temp_celsius:.2f}°C \nTemperature in {CITY} feels like: {feels_like_cel:.2f}°C \nHumidity in {CITY}: {humidity}% \nWind Speed in {CITY}: {wind_speed}m/s \nGeneral Weather in {CITY}: {desc} \nThe sun rises in {CITY} at: {sunrise_time} \nThe sun sets in {CITY} at: {sunset_time}", self)
        self.label_1.setStyleSheet("border :5px solid black; background-color: white;")  
        # moving position 
        self.label_1.move(50, 150) 
  
        # setting font and size 
        self.label_1.setFont(QFont('Arial', 28)) 

        # creating label
        self.label_2 = QLabel(self)
        self.pixmap = QPixmap(weatherimg)
        self.label_2.setPixmap(self.pixmap)
        self.label_2.move(1000,200)
        self.label_2.resize(200,200)
        
        self.label_4 = QLabel("Icon", self)
        self.label_4.setStyleSheet("border :3.5px solid black; background-color: white;")
        self.label_4.setFont(QFont('Arial', 24))
        self.label_4.move(1050,150)

        self.switch = QLabel(f"{city2} | {country}\n \n \n \n{temp_celsius2:.2f}°C | {desc2}", self)
        self.switch.setStyleSheet("color: white")
        self.switch.setAlignment(Qt.AlignCenter)
        self.switch.setFont(QFont('Arial Bold', 28))
        self.switch.move(100,475)
        self.switch.resize(500,250)
        
        self.switch2_label = QLabel(self)
        self.pixmap2 = QPixmap(weatherimg2)
        self.switch2_label.setPixmap(self.pixmap2)
        self.switch2_label.move(230,500)
        

class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(260, 120)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)
        


if __name__ == "__main__":
    new_city()
    app = QApplication(sys.argv)
    weatherimage()
    mw = MainWindow()
    mw.show()
    clock = DigitalClock()
    clock.show()

    def update_label():
        weatherimage()
        current_city = f"{city2} | {country}\n \n \n \n{temp_celsius2:.2f}°C | {desc2}"
        mw.switch.setText(current_city)
        mw.switch2_label = QLabel()
        mw.pixmap2 = QPixmap(weatherimg2)
        mw.switch2_label.setPixmap(mw.pixmap2)

    timer = QTimer()
    timer.timeout.connect(update_label)
    timer.start(5500)  # every 5,500 milliseconds
    sys.exit(app.exec_())

    