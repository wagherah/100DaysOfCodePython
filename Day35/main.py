# import requests
import os
# from twilio.rest import Client

################# TWILIO INFO #################
# account_sid = "AC15a37f750b117f6473d4c2f833161b71"
# auth_token = "ef7a82f69829009d00e99bbf8f7abf13"
#
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     messaging_service_sid='MG2eb9ed4bda56022b4321c327555108ac',
#     to='+923451911327',
#     body="Hello from Python!"
# )
#
#
# print(message.date_sent)

#
# OWM_END_POINT = "http://api.openweathermap.org/data/2.5/onecall"
# OWM_API_KEY = 'c6a76bfc3be337caee5023dcca4a2232'
#
# weather_params = {
#     "lat": 51.507351,
#     "lon": -0.127758,
#     "appid": OWM_API_KEY,
#     "exclude": "current,minutely,daily"
# }
#
# response = requests.get(OWM_END_POINT, params=weather_params)
# response.raise_for_status()
#
#
# weather_data = response.json()
# weather_slice = weather_data['hourly'][:12]
#
#
# will_rain = False
#
# for hour_data in weather_slice:
#     condition_code = hour_data['weather'][0]['id']
#     if int(condition_code) < 700:
#         # print('Bring an Umbrella')
#         will_rain = True
# if will_rain:
#     print('Bring an Umbrella')

print('Hello World')
