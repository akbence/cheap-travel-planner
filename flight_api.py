import requests
import json
import yaml


def get_api_key():
    with open('settings.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return(data.get("apikey"))

def cheapest_flight_in_month(origin,destination,depart_month):
    url = "https://api.travelpayouts.com/v1/prices/calendar"
    querystring = {"depart_date":depart_month,"origin":origin,"destination":destination,"currency":"EUR"}
    headers = {'x-access-token': get_api_key()}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text).get("data")

print(cheapest_flight_in_month("BUD","BCN","2019-11").get('2019-11-16'))



