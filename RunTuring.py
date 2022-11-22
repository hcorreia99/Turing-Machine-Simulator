from Tape import Tape


debug_run = False

print("Do not forget to setup input tape!")
print("Please input instructions file name: ")
filename = input()

# Load file instruction data

f = open(filename, "r")
tape = Tape(f)
f.close()

while not tape.running:
    pass