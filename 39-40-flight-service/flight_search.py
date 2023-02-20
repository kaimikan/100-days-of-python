import requests
from dotenv import load_dotenv
import os
import datetime as dt
from pprint import pprint

from notification_manager import NotificationManager


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, flight):
        self.flight = flight

    def find_flight(self, starting_code="LON"):
        tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"
        tequila_api_key = os.getenv("tequila_api_key")
        print()
        now = dt.datetime.now()
        then = now + dt.timedelta(days=30 * 3)
        date_today = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
        date_to = str(then.day) + "/" + str(then.month) + "/" + str(then.year)
        # print(date_today)
        # print(date_to)
        tequila_params = {
            "fly_from": starting_code,
            "fly_to": self.flight["iataCode"],
            "dateFrom": date_today,
            "dateTo": date_to,
            "curr": "BGN"
        }
        tequila_header = {
            "apikey": f"{tequila_api_key}",
            "accept": "application/json"
        }
        response = requests.get(url=tequila_endpoint, params=tequila_params,
                                headers=tequila_header)
        response.raise_for_status()
        all_data = response.json()['data']
        # pprint(all_data)
        try:
            data = all_data[0]
        except IndexError:
            print("Sorry, no flights available.")
        else:
            price = data['price']
            departure = data['utc_departure'].split("T")[0]
            country_from = data['countryFrom']['name']
            country_to = data['countryTo']['name']
            print(
                f"The cheapest flight from {country_from} to {country_to} costs {price}lv. and is on {departure}(Y-M-D)")

            if int(price) < self.flight['lowestPrice']:
                print("Found a new lowest price, updating sheet and sending sms...")
                notification_manager = NotificationManager()
                notification_manager.send_sms(flight=self.flight, data=data)
                self.flight['lowestPrice'] = int(price)
