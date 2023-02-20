from dotenv import load_dotenv
import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def update_flight_entry(self, entry_id, sheety_endpoint, sheety_header, json_data):
        url = f"{sheety_endpoint}" + "/" + f"{entry_id}"
        response = requests.put(url=url, headers=sheety_header,
                                json=json_data)
        response.raise_for_status()
        print(response.json())
