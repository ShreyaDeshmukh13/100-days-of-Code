import smtplib
import requests
import time
from datetime import datetime

MY_EMAIL = "shreyadesh01032004@gmail.com"
MY_PASSWORD ="apkl scgt qoxl ofxk"
MY_LAT = 18.520430
MY_LONG = 73.856743
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

def is_iss_overhead():
    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]

    #Your position is within +5 or -5 degrees of the iss position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5<= iss_longitude<=MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng" : MY_LONG ,
        "formatted" : 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data= response.json()
    sunrise =int( data["results"]["sunrise"].split("T")[1].SPLIE(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].SPLIE(":")[0])

    time_now = datetime.now().hour()

    if time_now >= sunset or  time_now <=sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg = "Subject : LOOK UP 👆 \n\n The ISS is above you in the sky."
        )