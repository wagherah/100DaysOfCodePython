import requests

location ={'lat': 34, 'lng': 71}

respose = requests.get(url="https://api.sunrise-sunset.org/json", params=location)
respose.raise_for_status()

data = respose.json()['results']['sunrise']
print(data)