'''
Challenge 2 - A Simple Terminal Interface
'''
USERS = [
  {
    "name": "Seongwoo Kim",
    "username": "skim",
    "location": "112"
  },
  {
    "name": "Sophia Bennett",
    "username": "sbennett",
    "location": "43"
  },
  {
    "name": "Leo Fernandez",
    "username": "lfernandez",
    "location": "118"
  },
  {
    "name": "Gabriel Santos",
    "username": "gsantos",
    "location": "341"
  },
  {
    "name": "Zhurong Chen",
    "username": "czhurong",
    "location": "203"
  },
  {
    "name": "Maya Rodriguez",
    "username": "mrodriguez",
    "location": "35"
  },
  {
    "name": "Srithi Patel",
    "username": "spatel",
    "location": "117"
  },
]

LOCATION_MAP = {
  "35": "Toronto, Canada",
  "43": "London, UK",
  "112": "Seoul, South Korea",
  "117": "Mumbai, India",
  "118": "Buenos Aires, Argentina",
  "203": "Shanghai, China",
  "341": "Rio de Janeiro, Brazil",
}

# Write your code below

import sys

if len(sys.argv) > 1:
  for arg in range(1,len(sys.argv)):
    for user in USERS:
      if user['username'] == sys.argv[arg]:
        name, username, location = user['name'], user['username'], LOCATION_MAP.get(user['location'], 'Unknown')
        print(f"{name}\n\tUsername: {username}\n\tLocation: {location}\n")
        break
    else:
      print(f'{sys.argv[arg]} not found.\n')
else:
  print("Please provide a username.")