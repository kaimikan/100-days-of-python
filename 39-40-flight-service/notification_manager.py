from twilio.rest import Client
import requests
from dotenv import load_dotenv
import os
import datetime as dt


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_sms(self, flight, data):
        price = data['price']
        departure = data['utc_departure'].split("T")[0]
        country_from = data['countryFrom']['name']
        country_to = data['countryTo']['name']

        sms_body = f"The cheapest flight from {country_from} to {country_to} costs {price}lv. and is on {departure}(Y-M-D)"

        trial_number = os.getenv("trial_number")
        my_number = os.getenv("my_number")
        account_sid = os.getenv("account_sid")
        auth_token = os.getenv("auth_token")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=my_number,
            body=sms_body,
            from_=trial_number
        )
        print(message.sid)
        pass
