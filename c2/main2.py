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
# I've re-written your code here instead. 
# A) Because I forgot to not use functions. Oops.
# B) Because it's easier to just re-write and it show what to do instead

import sys

if len(sys.argv) < 2:
  print('Not enough args')
  exit(1) # Error code 1 signifies an error. Error code 0 signifies no error

# By using the if statement above and short-circuiting early, we save ourselves from nesting our code even more
usernames = sys.argv[1:] # This makes it clear what we're getting from sys.argv

for username in usernames:
  user_found = False

  for user in USERS:
    if user['username'] == username:
      name, username, location = user['name'], user['username'], LOCATION_MAP.get(user['location'], 'Unknown')
      print(f"{name}\n\tUsername: {username}\n\tLocation: {location}\n")
      user_found = True
      break
    
  # Because we're breaking the loop, we don't need an else statement.
  # If the if statement fires off, the code will never get here,
  # so we can save ourselves from nesting. Hopefully by this point you can tell that
  # nesting == bad.
  if not user_found:
    print(f'{username} not found.\n')

