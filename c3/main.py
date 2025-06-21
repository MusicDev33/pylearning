import json, sys

'''
Challenge 3 - JSON Files and File Reading
'''
# Your code will start in here. If main needs parameters, feel free to add them
def import_userdb(file) -> dict:
  with open(file) as users:
    userdb = json.load(users)
    return userdb

def import_locationdb(file) -> dict:
  with open(file) as locations:
    locationdb = json.load(locations)
    return locationdb

def user_lookup(username: str, userdb: dict) -> dict | None:
  if username in userdb.keys():
    return userdb[username]
  else:
    print(f"User {username} not found.\n")
    return None

def loc_lookup(user: dict, locationdb: dict) -> str:
  location = user['loc_id']
  if location in locationdb.keys():
    return locationdb[location]
  else:
    return "Unknown"

def print_userinfo(user_data: dict, location: str):
  username, name = user_data['username'], user_data['name']
  print(name)
  print(f'  Username: {username}')
  print(f'  Location: {location}\n')
  
def main(users: list[str], userdb_filename: str, locationdb_filename: str):
  user_list =  users[1:]
  userdb = import_userdb(userdb_filename)
  locationdb = import_locationdb(locationdb_filename)
  if not user_list:
    print(r'No username(s) provided.')
    return None
  for user in user_list:
    u_data = user_lookup(user, userdb)
    if u_data:
      location = loc_lookup(u_data, locationdb)
      print_userinfo(u_data, location)

# What does this line do? Comment what it does in your code.
# It prevents the main() function from executing automatically if imported into another script
# So main() only runs if main.py is run directly or if called explicitly after being imported
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
  main(sys.argv, 'users.json', 'lmap.json')
