#
# Adavent of Code Template
#
import sys
import math

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

    #lines = []
    adaptors = []

    f = open(filename)
    for line in f:
        line = line.strip()
        #lines.append(line)
        adaptors.append(int(line))

    f.close()

    return adaptors


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# use all the asaptors to get max jolts
#
def useAllAdaptors(adaptors):
    jolts = [0,0,1]

    adaptors.sort()
    lastAdaptor = 0
    for adaptor in adaptors:
        jolt = adaptor - lastAdaptor
        jolts[jolt-1] += 1
        lastAdaptor = adaptor

    return jolts


#
# find all adaptor combinations
#
def findAdaptors(adaptors):

    adaptors.sort()
    lastAdaptor = 0
    options = []
    for a in range(len(adaptors)):
        jolt = adaptors[a] - lastAdaptor
        mod = 1
        if jolt == 1:
            if a+1 < len(adaptors) and adaptors[a+1] - lastAdaptor <= 3:
                mod += 1
            if a+2 < len(adaptors) and adaptors[a+2] - lastAdaptor <= 3:
                mod += 1

        options.append(mod)

        lastAdaptor = adaptors[a]

    #print(options)
    options.reverse()
    options.append(1)

    lastnums = [1 for _ in range(max(options))]
    group = 0
    groups = []
    for option in options:
        #print(option)
        if option == 1:
            if group > 1:
                groups.append(group)
                group = 0
                lastnums = [1 for _ in range(max(options))]
        else:
            group = 0
            for p in range(option):
                group += lastnums[p]
            lastnums.pop()
            lastnums.insert(0,group)
            #print(lastnums)

    #print(groups)
    return math.prod(groups)


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
    adaptors = loadData(filename)
    print(" Adaptors Read: ", len(adaptors))
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    jolts = useAllAdaptors(adaptors)
    print(jolts)
    answer = jolts[0] * jolts[2]
    print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = findAdaptors(adaptors)
    print()
    print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
