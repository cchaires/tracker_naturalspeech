import requests
import datetime as dt
import os
from dotenv import load_dotenv
import ui

load_dotenv()
X_APP_ID = os.getenv("X_APP_ID")
X_APP_KEY = os.getenv("X_APP_KEY")
X_REMOTE_USER = os.getenv("X_REMOTE_USER_ID")
AUTHORIZATION_KEY = os.getenv("AUTHORIZATION")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY,
    "x-remote-user-id": X_REMOTE_USER
}
user_query = input("What exercise did you do\n?")

nutritionix_params = {
    "query": user_query,
    "gender": "male",
    "weight_kg": 80.5,
    "height_cm": 169.64,
    "age": 32
}

response_nutritionix = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_params)
response_nutritionix_json = response_nutritionix.json()
print(response_nutritionix_json)

TODAY = str(dt.datetime.now().day) + "/" + str(dt.datetime.now().month) + "/" + str(dt.datetime.now().year)
TIME = dt.datetime.now().time().strftime("%H:%M:%S")
print(TIME, TODAY)
sheety_endpoint = "https://api.sheety.co/d902c2d4b30f97095a96290aec50a74b/pythonWorkout/workouts"

sheety_headers = {
    "Authorization": AUTHORIZATION_KEY
}


def post_multiple_workouts():
    for i in range(len(response_nutritionix_json['exercises'])):
        sheety_POST_params = {
            "workout": {
                "date": TODAY,
                "time": TIME,
                "exercise": response_nutritionix_json["exercises"][i]["name"],
                "duration": response_nutritionix_json["exercises"][i]["duration_min"],
                "calories": response_nutritionix_json["exercises"][i]["nf_calories"]
            }
        }
        response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_POST_params)
        print(response.status_code)


ui_window = ui.UI()
post_multiple_workouts()
