import http.client
import config

conn = http.client.HTTPSConnection("flight-fare-search.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': f"{config.api_key}",
    'X-RapidAPI-Host': "flight-fare-search.p.rapidapi.com"
}

conn.request("GET", "/v2/airport/departures?airportCode=ATL&date=2023-05-17&carrierCode=DL", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))