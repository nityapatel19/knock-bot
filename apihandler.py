"""
https://rapidapi.com/orthosie/api/knock-knock-jokes

"""
import json

import requests

url = "https://knock-knock-jokes.p.rapidapi.com/knock-knock/random"
url = "http://api.jokes.one/jod?category=knock-knock"

headers = {
    'x-rapidapi-host': "knock-knock-jokes.p.rapidapi.com",
    'x-rapidapi-key': "2c73e0efa1msh1141498ccf1cbbcp11c3c8jsnef8cbfe7fca6"
}

# response = requests.request("GET", url)
# joke = json.loads(response.text)
# print(joke)
