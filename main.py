import requests
from twilio.rest import Client

API_KEY = "your Weather API Key"
ACC_SID = "your Twilio Account SID"
AUTH_TOKEN = "your Twilio Account Token"

# your location's latitude and longitude
LAT = 31.278069 
LONG = 72.331673

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

id_1 = int(data["list"][0]["weather"][0]["id"])
id_2 = int(data["list"][1]["weather"][0]["id"])
id_3 = int(data["list"][2]["weather"][0]["id"])
id_4 = int(data["list"][3]["weather"][0]["id"])

# id less than 701 indicates rainy weather or snow
if id_1 < 701 or id_2 < 701 or id_3 < 701 or id_4 < 701:
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages.create(
        body= "Its going to rain today. Remember to bring an umbrella!",
        from_="the number given by twilio",
        to="your personal phone number"
    )
    print(message.status)
else:
    print("No rain expected")
