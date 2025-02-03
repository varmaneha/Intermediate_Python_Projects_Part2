import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "Accjdckn" #Your twilio sid
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 51.507351,
    "lon":-0.127758,
    "appid": api_key,
    "cnt": 4,
    }

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Its going to rain today. remember to bring an umbrella",
            from_="+121324354545",
            to="Your verified number"
        )
    print(message.status)

