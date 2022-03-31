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
    contains = {}
    parents = {}

    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)

        containPos = line.find("contain")
        bag = line[:containPos-6]
        containedbags = contains.setdefault(bag,[])

        if not line.endswith("no other bags."):
            bags = line[containPos+7:].split(",")
            for b in bags:
                parts = b.strip().split(" ")
                containqty = int(parts[0])
                containbag = parts[1] + " " + parts[2]
                containedbags.append((containbag,containqty))
                parents.setdefault(containbag,[]).append(bag)

    f.close()

    return contains, parents, lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# walk the tree looking for new colors
#
def containedColor(bag, parents, bagColors):

    bagParents = parents.get(bag, [])

    for bagParent in bagParents:
        if bagParent not in bagColors:
            bagColors.append(bagParent)
            bagColors = containedColor(bagParent, parents, bagColors)

    return bagColors


#
# Count the number of color bags that can contain the one passed
#
def colorBags(parents, bag):

    bagColors = [bag]

    bagColors = containedColor(bag, parents, bagColors)

    return len(bagColors) - 1


#
# walk the tree looking for new colors
#
def nestedColor(bag, contains):

    bags = 0

    bagChildren = contains.get(bag, [])

    for bagChild in bagChildren:
            childBags = nestedColor(bagChild[0], contains)
            bags += bagChild[1] + childBags * bagChild[1]

    return bags


#
# Count the number of color bags that can be inside the one passed
#
def insideBags(contains, bag):

    bags = nestedColor(bag, contains)

    return bags


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
    contains, parents, lines = loadData(filename)
    print(" Lines Read: ", len(lines))
    print("   Contains: ", len(contains))
    print("    Parents: ", len(parents))
    print()
    #print(contains.keys())
    #print(parents.keys())
    #printLines(lines)

    # Do Part 1 work
    print()
    answer = colorBags(parents, "shiny gold")
    print()
    print("{}Color Bags: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = insideBags(contains, "shiny gold")
    print()
    print("{}Inside Bags: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
