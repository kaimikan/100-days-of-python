import requests
import datetime as dt
import smtplib
import time

# # Status codes:
# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

TEST_LAT = 51.507351
TEST_LONG = -0.127758


def is_it_nighttime():
    # Sunset and Sunrise Times API
    parameters = {
        "lat": 2,
        "lng": 3,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # this is the original format for these: 2023-02-10T18:04:42+00:00
    # we want to only get the hour
    # keep in mind this returns UTC/GMT+0000 time, so you can adjust it for your timezone
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] + 2
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0] + 2

    time_now = dt.datetime.now().hour

    if time_now > sunset or time_now < sunrise:
        return True


def is_the_iss_above_you():
    # ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # # we will do this with the requests module instead - response.raise_for_status()
    # if response.status_code == 404:
    #     raise Exception("The resource does not exist")
    # elif response.status_code == 401:
    #     raise Exception("Not authorized to connect to data ")
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # is the test position within 5 degrees of the iss
    if iss_latitude + 5 >= TEST_LAT >= iss_latitude - 5 and \
            iss_longitude + 5 >= TEST_LONG >= iss_longitude - 5:
        return True


# check every 60 secs
while True:
    time.sleep(60)
    if is_the_iss_above_you() and is_it_nighttime():
        my_email = "secret-email@gmail.com"
        # this is from the gmail special account setup
        password = "secret"

        # connection = smtplib.SMTP("smtp.gmail.com")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # encrypt connection
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="secret@gmail.com",
                                msg="Subject: IT ARRIVED!\n\nthe ISS is somewhere in the night sky, take a peek!")
