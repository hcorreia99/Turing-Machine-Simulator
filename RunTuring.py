from Tape import Tape


debug_run = False
default_file_names = True

def debug_print():
    print(tape.current_state.__str__())
    print("Current Value / Position: " + tape.get() + " / " + str(tape.position))
    print(tape)
    input()

if default_file_names:
    input_filename="input.txt"
    instructions_filename = "addition.txt"
    output_filename = "output.txt"
else:
    print("Input file name: ")
    print("Instructions file name: ")
    instructions_filename = input()
    print("Output file name: ")
    output_filename = input()
if debug_run:
    print("Initiating debug run!")

tape = Tape(input_filename, instructions_filename, output_filename)

# Run loop
while tape.running:
    if debug_run:
        debug_print()
        input()
    tape.analyze()

if debug_run:
        debug_print()
        input()
