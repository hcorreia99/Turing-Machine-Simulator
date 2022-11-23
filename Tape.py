from State import State
class Tape:
    def __init__(self) -> None:
        self.tape = []
        self.position = 0
        self.states = []
        self.running = True
    
    def populate(self, input, states):
        self.populate_input(input)
        self.populate_states(states)

        # Select first state as starting state
        self.current_state = self.states[0]

    # Populates the tape
    def populate_input(self, input):
        for s in input:
            self.tape.append(s)
        self.tape.append("_")

    # Receives an array of states and populates
    def populate_states(self, states):
       for s in states:
            self.states.append(State(s))

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
    

    # Change state to state with state_name
    # If state_name is END tape stops running
    def changeState(self, state_name):
        for s in self.states:
            if s.name == state_name:
                self.current_state = s
                break
        # Check if new state is an END state
        if self.current_state.name == "END":
            self.end()

    # Ends this tape's run and output to file
    def end(self):
        self.running = False
        
    # Analyzes and acts on current slot with current state
    def analyze(self):
        if self.position==len(self.tape):
            self.tape.append("_")
        for c in self.current_state.conditions:
            if c.isValid(self.get()):
                self.set(c.new_value)
                self.move(c.move)
                return self.changeState(c.next_state)
                

    def __str__(self) -> str:
        return self.tape.__str__()

    
