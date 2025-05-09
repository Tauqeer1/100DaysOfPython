import requests

response =  requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400")
response.raise_for_status()

data = response.json()
print(data)