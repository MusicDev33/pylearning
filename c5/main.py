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

# ALT FUNCTION
def read_input_validation_alt(args: list[str]):
  # You got an args parameter, but you didn't use it.
  # Best practice is to handle sys.argv elsewhere, and then pass around the processed
  # version of it (usually called args)
  if len(args) == 2:
    return True
  
  # No need for an else statement if the if statement returns.
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
  
def write_input_validation_alt(args: list[str]):
  # Let's filter out the conditions we DON'T want, and then that allows us to write logic
  # that isn't nested
  if len(args) != 3:
    print(f'Error: Write mode expected two arguments. {str(len(args)-1)} arguments given.')
    return False
  
  name_data = args[1].split()
  location_data = args[2].split(', ')
  if ',' in args[1]:
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

def print_help():
  print('Read Mode:\n\tpython3 main.py -r username')
  print(f'Write Mode:\n\tpython3 main.py -w "Firstname Lastname" "City, Country"')

# ALT FUNCTION
# This would just go under the if __name__ == "__main__":
def main():
  # The first value of sys.argv isn't something we care about, so let's get rid of it
  args = sys.argv[1:]

  if len(args) < 2:
    print('Error: No mode specified.')
    print_help()
    return
  
  # Makes it very clear what args[0] is for. This isn't strictly necessary, but again,
  # keeping readability in mind, this is always nice
  flag = args[0]
  if flag == '-r': # Read mode
    if read_input_validation(args):
      db.get_user(args[1])
    return

  elif flag == '-w': # Write mode
    if write_input_validation(args):
      name = args[1]
      location = args[2]
      db.create_user(name, location)
    return
  
  # This is an easier way of checking. Easier to read too
  elif flag in ['-h', 'help']: # Help mode
    print_help()
    return

  print('Error: Invalid syntax.')
  print_help()

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