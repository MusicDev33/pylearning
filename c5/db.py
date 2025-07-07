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

# User Methods
def get_user(username: str):
  users = read_to_dict("_uindex.json")
  if username in users:
    user_id = users[username]

    userdb = read_to_dict('_users.json')
    user_data = userdb[user_id]
    name, username, location_id = user_data['name'], user_data['username'], user_data['location']

    locationdb = read_to_dict('_locations.json')
    location = locationdb[location_id]['name']

    print(name)
    print(f'  Username: {username}')
    print(f'  Location: {location}')
  else:
    print(f'User {username} not found.')

# ALT FUNCTION
def get_user_alt(username: str):
  users = read_to_dict("_uindex.json")
  if username not in users:
    # Short-circuit early. This makes code easier to read because there's less nesting.
    print(f"User {username} not found.")
    return # Exit the function

  # Now we're free to write whatever we want here because we've handled the user not existing
  user_id = users[username]

  userdb = read_to_dict('_users.json')
  user_data = userdb[user_id]
  name, username, location_id = user_data['name'], user_data['username'], user_data['location']

  locationdb = read_to_dict('_locations.json')
  location = locationdb[location_id]['name']

  print(name)
  print(f'  Username: {username}')
  print(f'  Location: {location}')

def create_user(name: str, location: str):
  name_data = name.split()
  username = name_data[0][0].lower() + name_data[1].lower()

  users = read_to_dict('_uindex.json')
  if username in users:
    print(f'Error: User with username {username} already exists. Failed to create new user.')
    return None

  locations = read_to_dict('_lindex.json')
  if location in locations:
    location_id = locations[location]
  else:
    create_location(location)
    locations = read_to_dict('_lindex.json')
    location_id = locations[location]

  user_id = str(uuid.uuid4())
  users[username] = user_id
  write_dict('_uindex.json', users)

  userdb = read_to_dict('_users.json')
  user_data = {user_id:{'username': username, 'name': name, 'location': location_id, 'id': user_id}}
  userdb.update(user_data)
  write_dict('_users.json', userdb)
  get_user(username)
  print('User created successfully.')

# ALT FUNCTION
def create_user_alt(name: str, location: str):
  # Be explicit with how you want to split something
  # By not specifying, your program will also split by tabs and newlines too
  first_name, last_name = name.split(' ')

  # save ourselves some brackets here
  # Code is read more often than it is written, so always be thinking of readability, especially in Python
  username = first_name[0].lower() + last_name.lower()

  users = read_to_dict('_uindex.json')
  if username in users:
    print(f'Error: User with username {username} already exists. Failed to create new user.')
    return # No need to specify None, as a normal return statement returns None by default
  
  locations = read_to_dict('_lindex.json')
  if location in locations:
    location_id = locations[location]
  else:
    create_location(location)
    locations = read_to_dict('_lindex.json')
    location_id = locations[location]

  user_id = str(uuid.uuid4())
  users[username] = user_id
  write_dict('_uindex.json', users)

  userdb = read_to_dict('_users.json')

  # Put spaces after your colons, it makes things easier to read
  user_data = {user_id: {'username': username, 'name': name, 'location': location_id, 'id': user_id}}
  userdb.update(user_data)
  write_dict('_users.json', userdb)
  get_user(username)
  print('User created successfully.')
