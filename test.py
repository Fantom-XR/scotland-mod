import json

test = '''{
  "usernames": [
    "I_nstict"
  ],
  "excludeBannedUsers": false
}'''

import requests
import emoji

api = requests.post('https://users.roblox.com/v1/usernames/users' , data =test, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})


#print(api.json()["data"][0]["id"])
hi = api.json()["data"][0]["id"]
hi1 = api.json()["data"][0]["displayName"]

print(hi)
print(hi1)

api = requests.get(f'https://users.roblox.com/v1/users/{hi}')
print(api.json()['description'])