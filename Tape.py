from State import State
class Tape:
    def __init__(self, input_filename, instruction_filename, output_filename) -> None:
        # Populate tape
        self.tape = []
        f = open(input_filename, "r")
        self.populate(f)
        f.close()

        self.position = 0

        # Populate States
        self.states = []
        f = open(instruction_filename, "r")
        for line in f:
            self.states.append(State(line))
        f.close()

        self.current_state = self.states[0]
        self.running = True
        self.output_filename = output_filename

    # Decide wether to move left or right
    def move(self, move):
        if move == "R":
            self.right()
        elif move=="L":
            self.left()

    # Move one slot to the left
    def left(self):
        self.position-=1

    # Move one slot to the right
    def right(self):
        self.position+=1

    # Get value of current slot
    def get(self):
        return self.tape[self.position]

    # Set value of current slot
    def set(self, value):
        self.tape[self.position] = value
    
    def populate(self, file):
        arr=file.read()
        for a in arr:
            self.tape.append(a)
        self.tape.append("_")

    # Change state to state with state_name
    # If state_name is END tape stops running
    def changeState(self, state_name):
        for s in self.states:
            if s.name == state_name:
                self.current_state = s
                break
        if self.current_state.name == "END":
            self.running = False

    # Ends this tape's run
    def end(self):
        self.end_state = True
        f = open(self.output_filename,"a")
        result = ""
        for s in self.tape:
            result += s
        f.write(result)
        f.close()
        

    # Analyzes and acts on current slot with current state
    def analyze(self):
        for c in self.current_state.conditions:
            if c.isValid(self.get()):
                self.set(c.new_value)
                self.move(c.move)
                self.changeState(c.next_state)
                break

    def __str__(self) -> str:
        return self.tape.__str__()

    
