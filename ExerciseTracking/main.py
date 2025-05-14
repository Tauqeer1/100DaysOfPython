import requests

NUTRITION_APP_ID = "f2e6436f"
NUTRITION_API_KEY = "f74110b8ad672d20bae9739533a2e6d6"


url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

payload_body = {
    'query': input("Tell me which exercise you did: ")
}

req_headers = {
    'x-app-id': NUTRITION_APP_ID,
    'x-app-key': NUTRITION_API_KEY,
}

req = requests.post(url, json=payload_body, headers=req_headers)
req.raise_for_status()
res = req.json()

print(res)