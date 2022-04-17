# CLAGy

CLAGy is a CLAG interpreter and transpiler to brainfuck.

## The CLAG Language

CLAG is a derivative of the brainfuck programming language, Where every command looks exactly the same. This is because all commands are made from 4 characters: the Cyrillic "о", the Latin "o", the Armenian "օ", and the Greek "ο". CLAG uses a single infinite array of positive integers to store all values, with a pointer to the current cell.

[Find out more about CLAG](https://esolangs.org/wiki/CLAG)

## Usage

To run a CLAG program with the interpreter:
  
  ```clag.py run (program path)```

To transpile a clag program to brainfuck:

  ```clag.py to_bf (program path)```

