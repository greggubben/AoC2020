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
# Print the seats
#
def printSeats(seats):

    for seat in seats:
        print("row", color.YELLOW, seat[1], color.END, ", column", color.YELLOW, seat[2], color.END, ", seat ID", color.YELLOW, seat[0], color.END)


#
# find the row from the row section of the boarding pass
#
def findRow(rowStr):
    section = 128
    row = 0
    endRow = 127

    for c in rowStr:
        section = section // 2
        if c == "F":
            endRow -= section
        elif c == "B":
            row += section
        else:
            print(color.RED, "Bad ROW Character", c, color.END)

    return row


#
# find the col from the col section of the boarding pass
#
def findCol(colStr):
    section = 8
    col = 0
    endCol = 7

    for c in colStr:
        section = section // 2
        if c == "L":
            endCol -= section
        elif c == "R":
            col += section
        else:
            print(color.RED, "Bad COL Character", c, color.END)

    return col


#
# Find the seats from the boarding passes
#
def findSeats(boardingPasses):

    seats = []

    for boardingPass in boardingPasses:
        row = findRow(boardingPass[:7])
        col = findCol(boardingPass[7:])
        seatID = row * 8 + col
        seats.append((seatID, row, col))

    return seats


#
# Find my seat
#
def findSeat(seats):

    for s in range(len(seats)-1):
        currSeat = seats[s]
        nextSeat = seats[s+1]
        if currSeat[0] + 2 == nextSeat[0]:
            break

    print("currSeat", currSeat)
    print("nextSeat", nextSeat)

    return currSeat[0]+1


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
    lines = loadData(filename)
    print(" Lines Read: ", len(lines))
    print()
    printLines(lines)

    # Do Part 1 work
    print()
    seats = findSeats(lines)
    seats.sort()
    #printSeats(seats)
    answer = seats[len(seats)-1][0]
    print()
    print("{}Highest Seat ID: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = findSeat(seats)
    print()
    print("{}My Seat ID: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
