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
    expenses = []

    f = open(filename)
    for line in f:
        line = line.strip()
        expenses.append(int(line))
        lines.append(line)

    f.close()

    return expenses, lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Find the 2 numbers that sum 2020
#
def findSum2(numbers, total):
    first = 0
    second = 0

    for f in range(len(numbers)-1):
        first = numbers[f]
        for s in range(f+1, len(numbers)):
            second = numbers[s]
            if first + second == total:
                return first, second
            elif first + second > total:
                break

#
# Find the 3 numbers that sum 2020
#
def findSum3(numbers, total):
    first = 0
    second = 0
    third = 0

    for f in range(len(numbers)-2):
        first = numbers[f]
        for s in range(f+1, len(numbers)-1):
            second = numbers[s]
            for t in range(s+1, len(numbers)):
                third = numbers[t]
                if first + second + third == total:
                    return first, second, third
                elif first + second + third > total:
                    break
            if first + second > total:
                break


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
    expenses, lines = loadData(filename)
    print(" Lines Read: ", len(lines))
    print()
    printLines(lines)
    print()

    # Do Part 1 work
    print()
    expenses.sort()
    first, second = findSum2(expenses,2020)
    answer = first * second
    print()
    print("{}Answer: {} * {} = {}{}{}".format(color.CYAN, first, second, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    first, second, third = findSum3(expenses,2020)
    answer = first * second * third
    print()
    print("{}Answer: {} * {} * {} = {}{}{}".format(color.CYAN, first, second, third, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
