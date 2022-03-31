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
    numbers = []

    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)
        numbers.append(int(line))

    f.close()

    return numbers, lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Check if number is invalid
#
def checkValid(number, previous):

    for x in range(len(previous)-1):
        for y in range(x+1, len(previous)):
            #print(" ", number, x, y, previous[x], previous[y])
            if number == previous[x] + previous[y]:
                return True
    return False


#
# Find the first invalid number
#
def findFirstInvalid(numbers, preamble):

    for ptr in range(preamble+1,len(numbers)):
        startPre = ptr - preamble - 1
        #print(ptr, startPre)
        if not checkValid(numbers[ptr], numbers[startPre: ptr]):
            return numbers[ptr]


#
# Find contiguous set of at least 2 numbers to sum
#
def findContigSum(numbers, number):

    for x in range(len(numbers)-1):
        for y in range(x+1,len(numbers)):
            if number == sum(numbers[x:y+1]):
                return x, y

    return 0,0


#
# Main
#
def main():

    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: " + sys.argv[0] + " inputfile preamble");
        return
    filename = args[0]
    preamble = int(args[1])
    print("   Input File:", filename)
    print("Preamble Size:", preamble)
    print()

    # Load data
    numbers, lines = loadData(filename)
    print("   Lines Read: ", len(lines))
    print(" Numbers Size: ", len(numbers))
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    invalidNumber = findFirstInvalid(numbers, preamble)
    print()
    print("{}First Invalid Number: {}{}{}".format(color.CYAN, color.YELLOW, invalidNumber, color.END))

    # Do Part 2 work
    print()
    startPtr, endPtr = findContigSum(numbers, invalidNumber)
    #print(startPtr, endPtr, numbers[startPtr] , numbers[endPtr])
    answer = max(numbers[startPtr:endPtr+1]) + min(numbers[startPtr:endPtr+1])
    print()
    print("{}Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
