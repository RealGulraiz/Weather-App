import requests
from urllib3 import request
import json
import win32com.client as wincom


city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=62d5ab9ee7054a0d988120142242810&q={city}"
r = requests.get(url)
weatherDict = json.loads(r.text) #convert string into json data
print(str(weatherDict["current"]["temp_c"]) + " celsius") #printing temperature in celsius

#TEMPERTURE IN AUDIO (Windows)
speak = wincom.Dispatch("SAPI.SpVoice")
tempCelsius=weatherDict["current"]["temp_c"]
text = f"The current temperature in {city} is {tempCelsius} celsius"
speak.Speak(text)
