import requests
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv(".env")
token = os.getenv("pixela_token")
username = "kaimikan"
graph_id = "graph1"

# CREATE USER
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# response.raise_for_status()
# print(response.text)

# CREATE GRAPH
pixela_graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_params = {
    "id": graph_id,
    "name": "Test Graph",
    "unit": "test",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# CREATE GRAPH PIXEL ENTRY
pixela_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

now = dt.datetime.now()
# method 1
print(now.strftime("%Y%m%d"))
# method 2
# :02d means we allocate 0 spaces for the digit and fill the empty spaces with 0 if there are any
date = f"{now.year}{now.month:02d}{now.day:02d}"
print(date)
pixel_params = {
    "date": date,
    "quantity": "1"
}

# response = requests.post(url=pixela_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


# UPDATE GRAPH PIXEL ENTRY
pixela_update_pixel_endpoint = f"{pixela_pixel_endpoint}/{date}"
pixel_update_params = {
    "quantity": "2"
}

# response = requests.put(url=pixela_update_pixel_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

# DELETE GRAPH PIXEL ENTRY
pixela_delete_pixel_endpoint = f"{pixela_pixel_endpoint}/{date}"

# response = requests.delete(url=pixela_delete_pixel_endpoint, headers=headers)
# print(response.text)
