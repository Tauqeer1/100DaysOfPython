import requests
import datetime

NUTRITION_APP_ID = "f2e6436f"
NUTRITION_API_KEY = "f74110b8ad672d20bae9739533a2e6d6"


NUTRITION_API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutrition_payload_body = {
    'query': input("Tell me which exercise you did: ")
}

nutrition_req_headers = {
    'x-app-id': NUTRITION_APP_ID,
    'x-app-key': NUTRITION_API_KEY,
}

nutrition_req = requests.post(NUTRITION_API_ENDPOINT, json=nutrition_payload_body, headers=nutrition_req_headers)
nutrition_req.raise_for_status()
nutrition_res = nutrition_req.json()

date = (datetime.date.today()).strftime("%d/%m/%Y")
time = (datetime.datetime.now().time()).strftime("%H:%M:%S")



exercises = [
    {'workout':{
        'date': date,
        'time': time,
        'exercise': exercise['name'].title(),
        'duration': exercise['duration_min'],
        'calories': exercise['nf_calories']}}
    for exercise in nutrition_res['exercises'] ]


SHEETY_API_ENDPOINT = "https://api.sheety.co/a470ba0cb29fd6bd4fab11fc3955d7aa/workoutsTracking/workouts"


for exercise in exercises:
    sheety_req = requests.post(SHEETY_API_ENDPOINT, json=exercise)
    sheety_req.raise_for_status()
    sheety_res = sheety_req.json()
    print(sheety_res)