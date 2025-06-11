"""
Challenge 1 - Location Mapping
Get your instructions from the README and solve the challenge
"""
USERS = [
  {
    "name": "Seongwoo Kim",
    "location": "112"
  },
  {
    "name": "Sophia Bennett",
    "location": "43"
  },
  {
    "name": "Leo Fernandez",
    "location": "118"
  },
  {
    "name": "Gabriel Santos",
    "location": "341"
  },
  {
    "name": "Zhurong Chen",
    "location": "203"
  },
  {
    "name": "Maya Rodriguez",
    "location": "35"
  },
  {
    "name": "Srithi Patel",
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

# Included the if statement so an exception isn't raised if the USER dictionary
# is updated with a location that isn't included in the LOCATION_MAP dictionary
for user in USERS:
  if user["location"] in LOCATION_MAP:
    print(f"{user["name"]} - {LOCATION_MAP[user["location"]]}")