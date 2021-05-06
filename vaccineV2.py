import os
import requests
import time
from datetime import datetime
import pytz

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=201301&date=07-05-2021"
timeInSec = 5
serverStatus = "up"

while True:
    response = requests.get(url)
    if response.status_code != 200:
        if serverStatus == "up":
            os.system("say Server is down")
            serverStatus = "down"
            timeInSec = 300
            print("REQUEST STATUS = " + str(response.status_code))
            print("Server is down, will notify when server will be up again.\n   Be patient....")
    else:
        if serverStatus == "down":
            os.system("say Server is up")
            serverStatus = "up"
            print("Server is up again.\n   Will notify when schedule booking opens....")
        response = response.json()
        timeInSec = 5
        if len(response["sessions"]) != 0:
            os.system("say Schedule Booking OPEN")
            print("REGISTRATION OPEN AT TIME : " + str(datetime.now(pytz.timezone('Asia/Kolkata'))))
            print(response)
    time.sleep(timeInSec)
