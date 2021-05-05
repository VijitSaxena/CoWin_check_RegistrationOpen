import os
import requests
import time
from datetime import datetime
import pytz

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=324001&date=06-05-2021"
timeInterval = 5
while True:
    response = requests.get(url).json()
    if len(response["sessions"]) == 0:
        print("***  ***")
        timeInterval = 5
        pass
    else:
        print("REGISTRATION OPEN AT TIME : " + str(datetime.now(pytz.timezone('Asia/Kolkata'))))
        print(response)
        timeInterval = 5
        os.system("say Registration OPEN")
    time.sleep(timeInterval)
