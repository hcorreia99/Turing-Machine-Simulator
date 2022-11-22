class Condition:
    def __init__(self, value, new_value, move, next_state) -> None:
        self.value = value
        self.new_value = new_value
        self.move = move
        self.next_state = next_state

    def __init__(self, s) -> None:
        s=s.replace(';','')
        s=s.replace('\n','')
        self.value = s[:s.find(">")]
        s=s[s.find(">")+1:]
        s=s.split(",")
        self.new_value=s[0]
        self.move=s[1]
        self.next_state=s[2]

    def isValid(self, value):
        return value == self.value

    def __str__(self) -> str:
        return "Value: " + self.value + " \ New Value: " + self.new_value +  " \ Move: " + self.move + " \ Next State: " + self.next_state

class State:
    def __init__(self, name, conditions) -> None:
        self.name = name
        self.conditions = conditions

    def __init__(self, s) -> None:
        self.name = s[:s.find(":")]
        self.conditions = []
        if self.name == "END":
            return
        for c in s[s.find(":")+1:].split(";"):
            self.conditions.append(Condition(c))

    def __str__(self) -> str:

        result = "--STATE--\n"
        result += "Name: " + self.name + "\n"
        if self.name == "END":
            return result
        result+="Conditions: \n"
        for c in self.conditions:
            result += "    "+c.__str__()
            result+="\n"
        return result




