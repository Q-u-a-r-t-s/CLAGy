
def create_jump_table(tokens):
    jump_table = {}
    start_indexes = []

    index = 0
    for token in tokens:
        if token.type == 'loop_start':
            start_indexes.append(index)

        elif token.type == 'loop_end':
            start = start_indexes.pop()
            end = index
            jump_table[start] = end
            jump_table[end] = start
        index += 1

    return jump_table
