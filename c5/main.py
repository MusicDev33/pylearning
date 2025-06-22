'''
Challenge 5 - Modules and the Runway
'''
import db
import sys

def read_input_validation(args: list[str]):
  if len(sys.argv) == 3:
    return True
  else:
    print(f'Error: Read mode expected one argument. {str(len(sys.argv)-2)} arguments given.')
    return False

def write_input_validation(args: list[str]):
  if len(sys.argv) == 4:
    name_data = sys.argv[2].split()
    location_data = sys.argv[3].split(', ')
    if ',' in sys.argv[2]:
      print("Error: Invalid character in name argument.")
      print_help()
      return False
    if len(name_data) != 2:
      print("Error: Invalid name format.")
      print_help()
      return False
    if len(location_data) != 2:
      print("Error: Invalid location format.")
      print_help()
      return False
    return True
  else:
    print(f'Error: Write mode expected two arguments. {str(len(sys.argv)-2)} arguments given.')
    return False

def print_help():
  print('Read Mode:\n\tpython3 main.py -r username')
  print(f'Write Mode:\n\tpython3 main.py -w "Firstname Lastname" "City, Country"')


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print('Error: No mode specified.')
    print_help()

  elif sys.argv[1] == '-r': # Read mode
    if read_input_validation(sys.argv):
      db.get_user(sys.argv[2])

  elif sys.argv[1] == '-w': # Write mode
    if write_input_validation(sys.argv):
      name = sys.argv[2]
      location = sys.argv[3]
      db.create_user(name, location)
  
  elif sys.argv[1] == '-h' or sys.argv[1] == 'help': # Help mode
    print_help()

  else:
    print('Error: Invalid syntax.')
    print_help()