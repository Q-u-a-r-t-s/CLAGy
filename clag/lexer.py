from textwrap import wrap
from clag.syntax import valid_characters, commands, digits

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def format(file_string) -> list:
    """
    Removes all invalid characters, and returns a list of commands
    """
    program_string = ""
    for char in file_string:
        if char in valid_characters:
            program_string += char
    
    command_list = wrap(program_string, 2)
    return command_list

def lex(command_list):
    """
    Returns a list of tokens
    """
    token_list = []
    command = 0
    while command < len(command_list):

        if commands[command_list[command]] in ['increment_pointer', 'decrement_pointer']:
            length_counter = 0
            pointer_movement = 0

            while commands[command_list[command + length_counter]] in ['increment_pointer', 'decrement_pointer']:
                if commands[command_list[command + length_counter]] == 'increment_pointer':
                    pointer_movement += 1
                else:
                    pointer_movement -= 1
                length_counter += 1
            
            command += length_counter - 1
            token_list.append(Token('move_pointer', pointer_movement))
        
        elif commands[command_list[command]] in ['add_to_cell', 'subtract_from_cell']:
            length_counter = 0
            change_string = ''

            while command + length_counter + 1 < len(command_list) and command_list[command + length_counter+1] in digits :
                change_string += digits[command_list[command + length_counter+1]]
                length_counter += 1
            
            if commands[command_list[command]] == 'add_to_cell':
                change_value = int(change_string, base=8)
            else:
                change_value = int(change_string, base=8) * -1
            
            command += length_counter 
            token_list.append(Token('change_cell_value', change_value))

        elif commands[command_list[command]] in ['output_cell', 'get_input', 'loop_start', 'loop_end']:
            token_list.append(Token(commands[command_list[command]]))
        
        command += 1
    
    return token_list