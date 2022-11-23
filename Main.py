from Tape import Tape
from Utils import *
from RunSettings import *

input = read_file(input_filename)[0]
states = read_file(instructions_filename)

def setup():
    global tape
    tape = Tape()
    tape.populate(input, states)

def update():
    if debug_run:
        debug_print(tape)
    tape.analyze()
    if step_by_step:
        input()

def finish():
    debug_print(tape)

def main():
    setup()
    while tape.running:
        update()
        
    finish()

main()