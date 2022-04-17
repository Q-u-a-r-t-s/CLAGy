# All valid CLAG characters. о, o, օ and ο
valid_characters = [u'\u043e', u'\u006f', u'\u0585', u'\u03bf']

# All valid CLAG commands. Corresponds to brainfuck commands
commands = {
    u'\u043e\u043e': 'increment_pointer',
    u'\u043e\u006f': 'decrement_pointer',
    u'\u043e\u0585': 'add_to_cell',
    u'\u043e\u03bf': 'subtract_from_cell',
    u'\u006f\u043e': 'output_cell',
    u'\u006f\u006f': 'get_input',
    u'\u006f\u0585': 'loop_start',
    u'\u006f\u03bf': 'loop_end'
}

# All valid CLAG digits. 
digits = {
    u'\u0585\u043e': '0',
    u'\u0585\u006f': '1',
    u'\u0585\u0585': '2',
    u'\u0585\u03bf': '3',
    u'\u03bf\u043e': '4',
    u'\u03bf\u006f': '5',
    u'\u03bf\u0585': '6',
    u'\u03bf\u03bf': '7',
}