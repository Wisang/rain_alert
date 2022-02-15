import requests
from twilio.rest import Client

latitude = 37.566536
longitude = 126.977966
api_key = "0ac6385b09dc84bdc71c40aa28f89a72"

account_sid = "AC5d5d1d3bed511b084991b20279367956"
auth_token = "4b68fbec0fab46b8651caa0189a620f6"
phone_number = "+18596952590"



parameter = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall",
    params=parameter)

weather_data = response.json()

twelve_hour_data = weather_data["hourly"][:12]

need_to_bring_umbrella = False

for hour in twelve_hour_data:
    if hour["weather"][0]["id"] < 700:
        need_to_bring_umbrella = True

if need_to_bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain.",
        from_='+18596952590',
        to='+821023309854'
    )
    print(message.status)
else:
    print("no need_to_bring_umbrella")
