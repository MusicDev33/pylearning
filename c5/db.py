'''
The Database!
Put all database related code in here. The underscores in front of the JSON files don't mean anything, I just added them 
so that they would show up at the top alphabetically.

json Package Explainer
The json package has 4 main methods people use:
dump, dumps, load, and loads

json.load - Takes a file-like object and turns it into a dictionary
json.loads - Takes a string and turns it into a dictionary (the s at the end means string)

json.dump - Takes an object (a dictionary most the time) and turns it into a file-like object
json.dumps - Takes an object (a dictionary most the time) and turns it into a string

Stick with the string 
'''
import json
import uuid

def db_test():
  print("Modules are working!")

def read_to_dict(file_name: str) -> dict:
  f = open(file_name, "r")
  contents = f.read()
  f.close()

  return json.loads(contents)

def write_dict(file_name: str, d: dict):
  contents = json.dumps(d, indent=2) # Indent = 2 makes the JSON look pretty in the file.

  f = open(file_name, "w")
  f.write(contents)
  f.close()

# Location Methods
def get_location(location_id: str):
  locations = read_to_dict("_locations.json")
  return locations[location_id]

def create_location(name: str):
  name_data = name.split(",")
  city, country = name_data[0].strip(), name_data[1].strip() # strip removes all whitespace from the front and end of strings

  location_id = str(uuid.uuid4()) # Use UUID4 to generate all IDs. Also technically UUIDs are not strings, so you'll have to force convert
  locations = read_to_dict("_locations.json")
  locations[location_id] = {
    "city": city,
    "country": country,
    "name": name,
    "id": location_id
  }

  write_dict("_locations.json", locations)

  loc_index = read_to_dict("_lindex.json")
  loc_index[name] = location_id
  write_dict("_lindex.json", loc_index)

  return location_id
