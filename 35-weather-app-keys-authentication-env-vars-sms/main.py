import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# this file has been excluded by .gitignore
# the point is for the sensitive data to only be available locally
load_dotenv(".env")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)

open_weather_route = "https://api.openweathermap.org/data/3.0/onecall"
# need to wait a few days for openweather to confirm the key
api_key = os.getenv("api_key")
parameters = {
    "lon": -0.13,
    "lat": 51.51,
    "appid": api_key,
    # exclude these to only get the hourly weather
    "exclude": "current,minutely,daily"
}

response = requests.get(open_weather_route, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

hourly_forecasts = data["hourly"]
next_12_hours_forecasts = [hourly_forecasts[0:12]]

rain_upcoming = False

for forecast in next_12_hours_forecasts:
    # numbers below 700 represent some sort of rain, snow, storm etc.
    if int(forecast["weather"][0]["id"]) < 700:
        rain_upcoming = True

if rain_upcoming:
    # print("The weather calls for an umbrella-ela-ela e e e")
    message = client.messages.create(
        to=os.getenv("trial_number"),
        body='The weather calls for an umbrella-ela-ela e e e ☔',
        from_=os.getenv("my_number")
    )
    print(message.sid)
