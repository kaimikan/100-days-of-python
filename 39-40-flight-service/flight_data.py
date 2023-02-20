import requests
from dotenv import load_dotenv
import os
import datetime as dt
from pprint import pprint


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight):
        self.flight = flight
        self.add_iata_code()

    def add_iata_code(self):
        tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"
        tequila_api_key = os.getenv("tequila_api_key")
        tequila_params = {
            "term": self.flight["city"],
            "locale": "en-US",
            "location-types": "city",
            "limit": 10,
            "active_only": "false",
            "sort": "name"
        }
        tequila_header = {
            "apikey": f"{tequila_api_key}",
            "accept": "application/json"
        }
        response = requests.get(url=tequila_endpoint, params=tequila_params,
                                headers=tequila_header)  # , json={"workout": data})
        response.raise_for_status()
        # print(response.json())
        code = response.json()['locations'][0]['code']
        print(code)

        self.flight["iataCode"] = code
