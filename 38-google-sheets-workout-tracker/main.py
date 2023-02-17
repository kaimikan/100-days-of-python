import requests
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv(".env")
nutritionix_app_id = os.getenv("nutritionix_app_id")
nutritionix_app_key = os.getenv("nutritionix_app_key")

exercise_description = input("The exercises which you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": exercise_description,
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 178,
    "age": 23
}

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_app_key,
    "x-remote-user-id": "0"
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
response.raise_for_status()
print(response.json())

sheety_app_key = os.getenv("sheety_app_key")
sheety_bearer_string = os.getenv("sheety_bearer_string")
sheety_endpoint = f"https://api.sheety.co/{sheety_app_key}/myWorkouts/workouts"
sheety_header = {
    "Authorization": f"Bearer {sheety_bearer_string}"
}
exercises_data = []
now = dt.datetime.now()
for exercise in response.json()['exercises']:
    data = {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": exercise['name'],
        "duration": exercise['duration_min'],
        "calories": exercise['nf_calories'],
    }
    exercises_data.append(data)
    response = requests.post(url=sheety_endpoint, headers=sheety_header, json={"workout": data})
    response.raise_for_status()
    print(response.json())

print(exercises_data)
