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

# First off, don't comment stuff that's obvious. It just mucks up the code.
# People reading the code will know your if statement is there for error handling purposes
# Code that requires comments is really hairy stuff that isn't obvious at a glance
for user in USERS:
  # You can assign variables like this.
  # The reason I do this is because when using f-strings, you can't enclose double quotes inside double quotes
  # and if that does work, that's dangerous. It'll break on other versions of Python.
  # With this, our f-string looks way more readable too
  name, location_id = user["name"], user["location"]

  # All dictionaries have a .get function. The first argument is the key, the second argument
  # is what it should return if it can't find the key. It's actually really awesome
  location = LOCATION_MAP.get(location_id, "Location Undefined")

  print(f"{name} - {location}")
