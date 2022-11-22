from State import State
class Tape:
    def __init__(self, instruction_file) -> None:
        self.tape = []
        self.position = 0
        self.states = []
        for line in instruction_file:
            self.states.append(State(line))
        self.current_state = ""
        self.running = True

    def move(self, move):
        if move == "R":
            self.right()
        elif move=="L":
            self.left()

    def left(self):
        self.position-=1

    def right(self):
        self.position+=1

    def get(self):
        return self.tape[self.position]

    def set(self, value):
        self.tape[self.position] = value

    def populate(self, arr):
        self.tape = arr

    def changeState(self, state):
        for s in self.states:
            if s.name == state:
                self.current_state = s

    def end(self):
        self.end_state = True

    
