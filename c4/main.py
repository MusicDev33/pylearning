'''
Challenge 4 - Parsing Text
'''

def print_block(header: str, events: set, log):
    print(f'=== {header} ===', file=log)
    for event in events:
        # To not have to do this check, you should've removed extra whitespace
        # before you added lines. I recommend processing things as much as you need to before sticking them in your list,
        # that way when you do have a loop that does something else, you leave processing code
        # out of the loop and can instead just focus on whatever you're doing (printing in this case).
        if not event.endswith('\n'):
            event += '\n'
        print(event, end='', file=log)
    # Using print this way is a little wacky
    # It's not technically wrong, but people will have to do a double-take
    # on your code because this kind of thing isn't super common.
    print('', file=log)

def parse_log(log_filename: str):
    successes = set()
    warnings = set()
    errors = set()
    with open(log_filename) as log:
        timestamp_filter = ' []-:0123456789'
        for event in log.readlines():
            event = event.lstrip(timestamp_filter)
            if event.startswith('SUCCESS'):
                # This is wacky too. I genuinely had to do a double-take to see what you were doing here.
                # successes.add(''.join(event.split(':')[1:])) is more readable
                # It's more verbose, but it's more canonical, in that Python devs use this solution
                # to this problem, and are therefore used to seeing it in code.
                successes.add(event[len('SUCCESS: '):])
            elif event.startswith('WARNING'):
                warnings.add(event[len('WARNING: '):])
            elif event.startswith('ERROR'):
                errors.add(event[len('ERROR: '):])
    with open('parse.txt', 'w') as f_log:
        print_block('ERRORS', errors, f_log)
        print_block('WARNINGS', warnings, f_log)
        print_block('SUCCESSES', successes, f_log)

# Just some ways to shorten the code a bit. Your code is fine the way it is by the way. Explicit is good.
# What I'm going to show you is only something you'd do if you had maybe like, 5+ different categories instead of 3
def alt_parse_log(log_filename: str):
    # Python dictionaries are actually awesome and magic
    cat_dict = {
        'SUCCESS': set(),
        'WARNING': set(),
        'ERROR': set(),
    }
    with open(log_filename) as log:
        timestamp_filter = ' []-:0123456789'
        for event in log.readlines():
            event = event.lstrip(timestamp_filter)
            categories = ['SUCCESS', 'WARNING', 'ERROR']
            for c in categories:
                if event.startswith(c):
                    # We don't *have* to put this in a variable, but it certainly makes the code more readable
                    # Than just cat_dict[c].add(''.join(event.split(':')[1:]))
                    log_msg = ''.join(event.split(':')[1:])
                    cat_dict[c].add(log_msg)

    with open('altparse.txt', 'w') as f_log:
        for c in reversed(categories):
          print_block(f'{c}S', cat_dict[c], f_log)

parse_log('logs.txt')