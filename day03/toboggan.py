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
# expand a map to cover slope
#
def expandMap(initialMap, right, down):
    treeMap = []

    rep = (len(initialMap)//down)//(len(initialMap[0])//right) + 1
    for l in initialMap:
        treeMap.append(l * rep)

    return treeMap


#
# count the number of trees hit
#
def countTrees(treeMap, right, down):
    treesHit = 0

    row = 0
    col = 0

    for row in range(0, len(treeMap), down):
        if treeMap[row][col] == "#":
            treesHit += 1
        col += right

    return treesHit


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
    #printLines(lines)

    # Do Part 1 work
    print()
    print("Initial Map Size = ", "rows=", len(lines), "cols=",len(lines[0]))
    treeMap = expandMap(lines, 3, 1)
    print("Expanded Map Size = ", "rows=", len(treeMap), "cols=",len(treeMap[0]))
    answer = countTrees(treeMap, 3, 1)
    print()
    print("{}Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    treeMap = expandMap(lines, 7, 1)
    print()
    trees11 = countTrees(treeMap, 1, 1)
    print("Right 1, down 1 = ", trees11)
    trees31 = countTrees(treeMap, 3, 1)
    print("Right 3, down 1 = ", trees31)
    trees51 = countTrees(treeMap, 5, 1)
    print("Right 5, down 1 = ", trees51)
    trees71 = countTrees(treeMap, 7, 1)
    print("Right 7, down 1 = ", trees71)
    trees12 = countTrees(treeMap, 1, 2)
    print("Right 1, down 2 = ", trees12)
    answer = trees11 * trees31 * trees51 * trees71 * trees12
    print()
    print("{}Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
