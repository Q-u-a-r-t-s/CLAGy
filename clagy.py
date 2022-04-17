from sys import argv
from clag.interpreter import interpret
from clag.transpiler import to_bf


def run(path):
    """
    Runs CLAG interpreter
    """
    with open(path, 'r', encoding='utf-8') as f:
        program_string = f.read()
    
    interpret(program_string)
        
        
        

def transpile(path, target_language):
    """
    Transpiles to target_language. Assumes path language based on target_language
    """
    with open(path, 'r', encoding='utf-8') as f:
        program_string = f.read()
    
    if target_language == "to_bf":
        transpiled_program = to_bf(program_string)
    
    print(transpiled_program)


def help():
    print("To run a CLAG program: clagy.py run (path)")
    print("To transpile a CLAG program to brainfuck: clagy.py to_bf (input path) (output path)")


if __name__ == "__main__":
    if len(argv) == 1:
        help()
    elif argv[1] == 'help':
        help()
    elif argv[1] == "run":
        run(argv[2])
    elif argv[1] == "to_bf":
        transpile(argv[2], argv[1])