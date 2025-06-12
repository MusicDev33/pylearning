'''
Challenge 2 - A Simple Terminal Interface
'''
import sys

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
usernames = sys.argv[1:]

def get_users(username: str):
  for u in USERS:
    if u["username"] == username:
      user = u
      break

  return user

def print_user(user: dict | None):
  if not user:
    print('User not found!')
    return
  
  name, location_id, username = user["name"], user["location"], user["username"]
  location = LOCATION_MAP.get(location_id, "Location Undefined")

  print(name)
  print(f'  Username: {username}')
  print(f'  Location: {location}')

for u in usernames:
  user = get_users(u)
  print_user(user)
