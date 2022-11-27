# Turing Machine Simulator
A simple turing machine simulator in python

# Input File
Sets the initial values of the tape.
The character position in the file equals the position in the tape array.

# Instructions File
Gives the program the set of instructions to allow tape editing
The file is case sensitive.

Instruction file syntax should be as follows:
    e.g. 1:0>0,R,1;C>C,R,2
    
    Preceding the ':' character must be the name of said state.
    As we can see in the example, that state is called '1'.
    This names must not repeat, no two states can have the same name.

    After the character ':' should follow the conditions.
    Conditions must be separated by the character ';'
    In the example we have 2 conditions.

    Each condition must have a condition value, (value that must be in the tape for this condition to run),
    a new value, (value that will overwrite the previous slot value),
    a move, either R (right) or L (left), (the way the tape will move after its done replacing the value)
    and a new state (the name of the new state to which the tape will go after its done moving)

    The condition value must preceed a '>' character.
    The remaining 3 values, new value, move and new state must be separated by a ','
    and appear respectively in that order

    The new state name must be an existing state.

    Characters that cannot be used in the tape: ':' ',' '>' ';'

    The starting state will be the first state written in the file

    The end state must be called END and should have nothing else typed
    Should look like this

    '_' symbol is a blank space
    END:

    Allows blank spaces and blank lines

# Output File
After the tape reaches an END state the tape is outputed to an output file

# RunSettings.py
Use this file to set the parameters for runtime booleans such as debug runs or a step by step run
    