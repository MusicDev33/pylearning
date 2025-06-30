'''
Challenge 4 - Parsing Text
'''
def parse_log(file_name: str):
    parse_data = {
        'success': list(),
        'warning': list(),
        'error': list(),
    }

    # A matter of taste. I never forget to close files,
    # but with this way, you do run the risk of forgetting to close files.
    # I would push you toward using 'with', I just personally avoid nesting
    # wherever I can in my coding style. Also the 'r' is a matter of taste too.
    # I like it because it's explicit
    f = open(file_name, 'r')
    for line in f.readlines():
        line = line.split('] ')[1].strip()
        line_data = line.split(':')
        key, log_msg = line_data[0].lower(), ''.join(line_data[1:]).strip()

        # I wanted to use set, but I forgot that sets don't preserve order!
        # We now lose the order in which our events happen (very important for log files!)
        # So we do this instead
        if log_msg not in parse_data[key]:
          parse_data[key].append(log_msg)

    f.close()

    # Me trying to be clever. Did it work? Kinda
    labels = [
        ('error', 'ERRORS'), 
        ('warning', 'WARNINGS'), 
        ('success', 'SUCCESSES')
    ]

    f = open('smparse.txt', 'w')
    for key, label in labels:
        f.write(f'===== {label} =====\n')
        for line in parse_data[key]:
            f.write(f'{line}\n')

        f.write('\n')
    f.close()
        
# Generally good practice to use this. It feels silly on small scripts
# and generally doesn't matter, but for any non-trivial program that uses modules,
# you'll want this.
if __name__ == '__main__':
  parse_log('logs.txt')