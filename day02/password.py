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
# Check passwords
#
def validOccurrancePasswords(pwlist):

    validpw = 0

    for l in pwlist:
        parts = l.split(" ")
        pw = parts[2]
        char = parts[1][0]
        times = parts[0].split("-")
        minTimes = int(times[0])
        maxTimes = int(times[1])
        times = pw.count(char)
        if minTimes <= times and times <= maxTimes:
            validpw += 1

    return validpw


#
# Check passwords
#
def validPositionPasswords(pwlist):

    validpw = 0

    for l in pwlist:
        parts = l.split(" ")
        pw = parts[2]
        char = parts[1][0]
        times = parts[0].split("-")
        firstPos = int(times[0]) - 1
        secondPos = int(times[1]) - 1
        if firstPos < len(pw) and secondPos < len(pw) and \
                ((char == pw[firstPos] and char != pw[secondPos]) or \
                (char != pw[firstPos] and char == pw[secondPos])):
            validpw += 1

    return validpw


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

    # Do Part 1 work
    #printLines(lines)
    answer = validOccurrancePasswords(lines)
    print()
    print("{}Valid Occurrance Passwords: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = validPositionPasswords(lines)
    print()
    print("{}Valid Positional Passwords: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
