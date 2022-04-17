from clag.lexer import lex, format
from clag.parser import create_jump_table

def to_bf(program_string):
    tokens = lex(format(program_string))
    jump_table = create_jump_table(tokens)
    bf_program = ''

    for token in tokens:
        if token.type == 'move_pointer':
            if token.value > 0:
                bf_program += '>'*token.value
            else:
                bf_program += '<'*token.value
        
        elif token.type == 'change_cell_value':
            if token.value > 0:
                bf_program += '+'*token.value
            else:
                bf_program += '-'*token.value
        
        elif token.type == 'output_cell':
            bf_program += '.'
        
        elif token.type == 'get_input':
            bf_program += ','
        
        elif token.type == 'loop_start':
            bf_program += '['

        elif token.type == 'loop_end':
            bf_program += ']'
    
    return bf_program

