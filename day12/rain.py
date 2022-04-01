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

directions = ["N", "E", "S", "W"]
turn = {"R": 1, "L": -1}
rotate = {"R": (1,-1), "L": (-1,1)}
move = {"N": (-1,0), "E": (0,1), "S":(1,0), "W": (0, -1)}

#
# Load the file into a data array
#
def loadData(filename):

    instructions = []

    f = open(filename)
    for line in f:
        line = line.strip()
        instruction = line[0]
        value = int(line[1:])
        instructions.append((instruction,value))

    f.close()

    return instructions


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Move the Ship based on instructions
#
def moveShip (instructions):

    facing = "E"
    ns = 0
    we = 0
    steps = []
    steps.append((ns, we, facing))

    for i in instructions:
        instruction = i[0]
        value = i[1]
        if instruction in turn.keys():
            facing = directions[(len(directions) + (directions.index(facing) + ((value//90) * turn[instruction]))) % len(directions)]
        else:
            if instruction == "F":
                nsAdj, weAdj = move[facing]
            else:
                nsAdj, weAdj = move[instruction]
            ns += nsAdj * value
            we += weAdj * value
        steps.append((ns,we, facing))
        #print("{} {:>4}: ({:>5},{:>5}) {}".format(instruction, value, ns, we, facing))

    return steps


#
# Move the Waypoint based on instructions
#
def moveWaypoint (instructions):

    ns = 0
    we = 0
    wp_ns = -1
    wp_we = 10
    steps = []
    steps.append((ns, we, wp_ns, wp_we))

    for i in instructions:
        instruction = i[0]
        value = i[1]
        if instruction in turn.keys():
            nsAdj, weAdj = rotate[instruction]
            for t in range(value//90):
                wp_ns, wp_we = (wp_we * nsAdj, wp_ns * weAdj)
        elif instruction == "F":
            ns += wp_ns * value
            we += wp_we * value
        else:
            nsAdj, weAdj = move[instruction]
            wp_ns += nsAdj * value
            wp_we += weAdj * value
        steps.append((ns,we, wp_ns,wp_we))
        #print("{} {:>4} Ship: ({:>5},{:>5}) Waypoint: ({:>5},{:>5})".format(instruction, value, ns, we, wp_ns, wp_we))

    return steps


#
# Compute Manhatten distance
#
def computeManhatten(steps):
    return abs(steps[-1][0]) + abs(steps[-1][1])


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
    instructions = loadData(filename)
    print("Instructions Read: ", len(instructions))
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    steps = moveShip(instructions)
    answer = computeManhatten(steps)
    print()
    print("{}Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    steps = moveWaypoint(instructions)
    answer = computeManhatten(steps)
    print()
    print("{}Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
