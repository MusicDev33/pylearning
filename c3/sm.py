'''
Challenge 3 - JSON Files and File Reading
'''
import json
import sys

def read_users():
  f = open('users.json')
  contents = f.read()
  f.close()

  return json.loads(contents)

def read_lmap():
  f = open('lmap.json')
  contents = f.read()
  f.close()

  return json.loads(contents)

def get_user(username: str):
  user_data = read_users()
  return user_data[username]

def get_location(loc_id: str):
  lmap_data = read_lmap()
  return lmap_data[loc_id]

# Your code will start in here. If main needs parameters, feel free to add them
def main(username: str):
  user = get_user(username)
  name, loc_id = user['name'], user['loc_id']
  location = get_location(loc_id)

  print(name)
  print(f'  Username: {username}')
  print(f'  Location: {location}')

if __name__ == '__main__':
  username = sys.argv[1]
  main(username)
