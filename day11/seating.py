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

    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)

    f.close()

    return lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Print the floor
#
def printFloor(step, floor):

    print("---", step, "---")
    print("\n".join(floor))
    print()


#
# find neighboring occupied seats
#
def neighboringOccupied(row, col, floor):
    occupied = 0
    minRow = row - 1 if row > 0 else 0
    maxRow = row + 1 if row < len(floor)-1 else len(floor)-1
    minCol = col - 1 if col > 0 else 0
    maxCol = col + 1 if col < len(floor[row])-1 else len(floor[row])-1
    for r in range(minRow,maxRow+1):
        occupied += floor[r][minCol:maxCol+1].count("#")

    return occupied


#
# Return first non '.' string along path
#
def getSeat(row, rStep, col, cStep, floor):
    seat = "."

    while seat == ".":
        row += rStep
        col += cStep
        if 0 <= row and row < len(floor) and 0 <= col and col < len(floor[row]):
            seat = floor[row][col]
        else:
            break

    #print(" ", row, rStep, col, cStep, seat)
    return seat


#
# find diagonal occupied seats
#
def diagonalOccupied(row, col, floor):
    occupied = 0
    for rStep in [-1, 0, 1]:
        for cStep in [-1, 0, 1]:
            occupied += 1 if getSeat(row, rStep, col, cStep, floor) == "#" else 0

    return occupied


#
# Run model of people occupy or empty seats
#
def modelUntilStable(startFloor, occupants, occupiedFunction):

    floor = startFloor

    loop = 0
    change = True
    while change:
        change = False
        #printFloor(loop, floor)
        newFloor = floor.copy()
        for row in range(len(floor)):
            for col in range(len(floor[row])):
                if floor[row][col] != ".":
                    occupied = occupiedFunction(row, col, floor)
                    #print(row,col,floor[row][col], occupied)

                    if floor[row][col] == "L" and occupied == 0:
                        newFloor[row] = newFloor[row][:col] + "#" + newFloor[row][col+1:]
                        change = True
                    elif floor[row][col] == "#" and occupied > occupants:
                        newFloor[row] = newFloor[row][:col] + "L" + newFloor[row][col+1:]
                        #newFloor[row][col] = "L"
                        change = True

        floor = newFloor
        loop += 1
        #if loop > 5: break

    return loop-1, floor


#
# Count the number of occupied seats
#
def countOccupied(floor):

    occupied = 0
    for f in floor:
        occupied += f.count("#")

    return occupied


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
    floor = loadData(filename)
    print(" Floor: (", len(floor), ",", len(floor[0]), ")")
    print()
    #printLines(floor)

    # Do Part 1 work
    print()
    loops, stableFloor = modelUntilStable(floor, 4, neighboringOccupied)
    answer = countOccupied(stableFloor)
    print()
    print("Loops:", loops)
    print("{}Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    loops, stableFloor = modelUntilStable(floor, 5, diagonalOccupied)
    answer = countOccupied(stableFloor)
    print()
    print("Loops:", loops)
    print("{}Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
