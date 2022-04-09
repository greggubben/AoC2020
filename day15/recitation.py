#
# Adavent of Code Template
#
import sys
import os.path

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

    line = filename.strip()
    if os.path.exists(filename):
        f = open(filename)
        for line in f:
            line = line.strip()
        f.close()

    return [int(n) for n in line.split(",")]


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Play the game for specified turns using the starting numbers
#
def play(startingNumbers, maxTurns):
 
    turn = 0
    lastNumber = 0
    spokenNumbers = {}
    for startingNumber in startingNumbers:
        turn += 1
        spokenNumbers[startingNumber] = [turn,0]
        lastNumber = startingNumber
        #print("Turn:", turn, "Spoken:", startingNumber, "Starting")

    while turn < maxTurns:
        turn += 1
        #print(spokenNumbers)
        pastTurn = spokenNumbers[lastNumber]
        if pastTurn[1] == 0:
            spokenNumber = 0
        else:
            spokenNumber = pastTurn[0] - pastTurn[1]

        #print("Turn:", turn, "Spoken:", spokenNumber, "First" if spokenNumber == 0 else "Before")
        pastTurns = spokenNumbers.setdefault(spokenNumber,[0,0])
        pastTurns.insert(0,turn)
        pastTurns.pop()
        lastNumber = spokenNumber

    return lastNumber



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
    startingNumbers = loadData(filename)
    print("Starting Numbers: ", len(startingNumbers))
    print()
    printLines(startingNumbers)

    # Do Part 1 work
    print()
    answer = play(startingNumbers,2020)
    print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = play(startingNumbers,30000000)
    print()
    print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
