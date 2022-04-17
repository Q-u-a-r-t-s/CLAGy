from clag.lexer import lex, format
from clag.parser import create_jump_table

def interpret(program_string):

    tokens = lex(format(program_string))
    jump_table = create_jump_table(tokens)
    
    cells = [0]
    pointer = 0
    token_pointer = 0

    while token_pointer < len(tokens):
        token = tokens[token_pointer]
        if token.type == 'move_pointer':
            pointer += token.value

            while pointer >= len(cells):
                cells.append(0)
            
            while pointer < 0:
                cells.insert(0, 0)
                pointer += 1
            
        elif token.type == 'change_cell_value':
            if cells[pointer] + token.value < 0:
                raise Exception("Cells cannot have a value below 0")
            else:
                cells[pointer] += token.value
        
        elif token.type == 'output_cell':
            print(chr(cells[pointer]), end = '')
        
        elif token.type == 'get_input':
            cells[pointer] = sum(map(ord, input('\n> ')))
        
        elif token.type == 'loop_start' and cells[pointer] == 0:
            token_pointer = jump_table[token_pointer]
        
        elif token.type == 'loop_end':
            token_pointer = jump_table[token_pointer] -1
        
        token_pointer += 1