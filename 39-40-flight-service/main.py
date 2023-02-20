import requests
from pprint import pprint
from dotenv import load_dotenv
import os

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

# This file will need to use the DataManager,
# FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

load_dotenv(".env")
data_manager = DataManager()

sheety_app_key = os.getenv("sheety_app_key")
sheety_bearer_string = os.getenv("sheety_bearer_string")
sheety_endpoint = f"https://api.sheety.co/{sheety_app_key}/flightDeals/prices"
sheety_header = {
    "Authorization": f"Bearer {sheety_bearer_string}"
}
response = requests.get(url=sheety_endpoint, headers=sheety_header)  # , json={"workout": data})
response.raise_for_status()
flight_data = response.json()['prices']

# pprint(flight_data)

are_iata_codes_filled = False
if not flight_data[0]["iataCode"] == "":
    are_iata_codes_filled = True

# if there are no IATA codes we want to pass each record
# to the FlightSearch class and add it there
flights = []
if not are_iata_codes_filled:
    for flight in flight_data:
        flight_data = FlightData(flight)
        flights.append(flight_data.flight)
        # print(f"sending flight to {flight['city']}, {flight['iataCode']} for search")
        data_manager.update_flight_entry(flight['id'], sheety_endpoint, sheety_header,
                                         {"price": {"iataCode": flight["iataCode"],
                                                    "lowestPrice": flight["lowestPrice"]}})
else:
    for flight in flight_data:
        flight_search = FlightSearch(flight)
        flight_search.find_flight("SOF")
        flights.append(flight_search.flight)
        data_manager.update_flight_entry(flight['id'], sheety_endpoint, sheety_header,
                                         {"price": {"lowestPrice": flight["lowestPrice"]}})

pprint(flight_data)
