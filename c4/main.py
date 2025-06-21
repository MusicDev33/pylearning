'''
Challenge 4 - Parsing Text
'''

def print_block(header: str, events: set, log):
    print(f'=== {header} ===', file=log)
    for event in events:
        if not event.endswith('\n'):
            event += '\n'
        print(event, end='', file=log)
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
                successes.add(event[len('SUCCESS: '):])
            elif event.startswith('WARNING'):
                warnings.add(event[len('WARNING: '):])
            elif event.startswith('ERROR'):
                errors.add(event[len('ERROR: '):])
    with open('parse.txt', 'w') as f_log:
        print_block('ERRORS', errors, f_log)
        print_block('WARNINGS', warnings, f_log)
        print_block('SUCCESSES', successes, f_log)

parse_log('logs.txt')