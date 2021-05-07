import requests
import time
from datetime import datetime
import pytz
import pyttsx3

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=324001&date=08-05-2021"
timeInSec = 5
serverStatus = "start"
speechEngine = pyttsx3.init()

while True:
    response = requests.get(url)
    if response.status_code != 200:
        if serverStatus != "down":
            speechEngine.say("Server is down")
            speechEngine.runAndWait()
            serverStatus = "down"
            timeInSec = 300
            print("REQUEST STATUS = " + str(response.status_code))
            print("Server is down, will notify when server will be up again.\n   Be patient....")
    else:
        if serverStatus != "up":
            speechEngine.say("Server is up")
            serverStatus = "up"
            speechEngine.runAndWait()
            print("Server is up.\n   Will notify when schedule booking opens....")
        response = response.json()
        timeInSec = 5
        if len(response["sessions"]) != 0:
            speechEngine.say("Schedule Booking OPEN")
            speechEngine.runAndWait()
            print("REGISTRATION OPEN AT TIME : " + str(datetime.now(pytz.timezone('Asia/Kolkata'))))
            print(response)
    time.sleep(timeInSec)
