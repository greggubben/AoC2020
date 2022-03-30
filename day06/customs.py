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
    groups = []
    group = []
    groups.append(group)

    f = open(filename)
    for line in f:
        line = line.strip()
        if len(line) == 0:
            group = []
            groups.append(group)
        else:
            group.append(line)

        lines.append(line)

    f.close()

    return groups, lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# find unique yes by group
#
def findUniqueYes(groups):
    sumYes = 0

    for group in groups:
        questions = ""
        for person in group:
            for question in person:
                if questions.count(question) == 0:
                    questions += question

        sumYes += len(questions)

    return sumYes


#
# find all yes by group
#
def findAllYes(groups):
    sumYes = 0

    for group in groups:
        questions = ""
        answers = ""
        for person in group:
            for question in person:
                if questions.count(question) == 0:
                    questions += question
                answers += question

        for q in questions:
            if answers.count(q) == len(group):
                sumYes += 1

    return sumYes


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
    groups, lines = loadData(filename)
    print(" Lines Read: ", len(lines))
    print("     Groups: ", len(groups))
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    answer = findUniqueYes(groups)
    print()
    print("{}Unique Yes: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = findAllYes(groups)
    print()
    print("{}All Yes: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
