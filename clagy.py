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
    
    return to_bf(program_string)

if __name__ == "__main__":
    if argv[1] == "run":
        run(argv[2])
    elif argv[1] == "to_bf" or argv[1] == "to_clag":
        program = transpile(argv[2], argv[1])
        print(program)