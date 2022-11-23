# Readies a file's content for handling
def read_file(file_name):
    file = open(file_name,"r")
    content = file.read()
    file.close()
    # remove blank spaces
    content = content.replace(" ", "")

    # split by lines
    content = content.split("\n")
    for l in content:
        if l == "":
            content.remove(l)
    return content

def debug_print(tape):
    print(tape.current_state.__str__())
    print("Current Value / Position: " + tape.get() + " / " + str(tape.position))
    print(tape)