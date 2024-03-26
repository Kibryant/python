def format_phone(string: str):
    if len(string) != 11:
        return "Invalid string. Please provide an 11-digit numeric string."
    return '({}) {}-{}'.format(string[:2], string[2:7], string[7:])
