#
# Adavent of Code Template
#
import sys

# Global Variables

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#
# Load the file into a data array
#
def loadData(filename):

    lines = []
    instructions = []

    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)
        instruction, value = line.split(" ")
        instructions.append((instruction, int(value)))

    f.close()

    return instructions, lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Run until infinite loop detected
#
def runToLoop(instructions):
    acc = 0
    ptr = 0
    performed = []
    
    while ptr not in performed and ptr < len(instructions):
        performed.append(ptr)
        instruction, value = instructions[ptr]
        #print(ptr, instruction, value, acc)
        if instruction == "acc":
            acc += value
            ptr += 1
        elif instruction == "jmp":
            ptr += value
        else:
            ptr += 1

    return acc, ptr < len(instructions)


#
# Fis the instructions so it terminates
#
def fixInstructions(instructions):

    for ptr in range(len(instructions)):
        newInstructions = instructions.copy()
        instruction, value = newInstructions[ptr]
        if instruction == "acc":
            continue
        elif instruction == "nop":
            instruction = "jmp"
        elif instruction == "jmp":
            instruction = "nop"
        newInstructions[ptr] = (instruction, value)
        acc, loop = runToLoop(newInstructions)
        if not loop:
            break

    return acc


#
# Main
#
def main():

    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: " + sys.argv[0] + " inputfile");
        return
    filename = args[0]
    print("Input File:", filename)
    print()

    # Load data
    instructions, lines = loadData(filename)
    print("  Lines Read: ", len(lines))
    print("Instructions: ", len(instructions))
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    answer, loop = runToLoop(instructions)
    print()
    print("{}Accumulator before Loop: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = fixInstructions(instructions)
    print()
    print("{}Accumulator fixed Instructions: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
