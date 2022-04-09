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
    rules = {}
    myTicket = []
    nearbyTickets = []

    section = 0
    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)
        if len(line) == 0:
            # blank line between sections
            section += 1

        elif section == 0:
            # rules
            field, parts = line.split(":")
            rule = []
            rules[field] = rule
            parts = parts.strip()
            ranges = parts.split(" or ")
            for ran in ranges:
                start,end = ran.split("-")
                rule.append((int(start),int(end)))

        elif section == 1:
            # my ticket
            if not line.startswith("your"):
                myTicket = [int(x) for x in line.split(",")]

        elif section == 2:
            # nearby tickets
            if not line.startswith("nearby"):
                nearbyTickets.append([int(x) for x in line.split(",")])

    f.close()

    return rules, myTicket, nearbyTickets, lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# check ticket against rules
#
def validateTicket(rules, ticket):
    invalidValues = []

    for value in ticket:
        #print(value)
        valid = False
        for rule in rules.keys():
            #print(rule)
            for start, end in rules[rule]:
                if start <= value and value <= end:
                    valid = True
                    break
            if valid: break
        if not valid:
            invalidValues.append(value)
            #print("Invalid", value)
            
    return invalidValues


#
# Scan tickets for valid data based on rules
#
def scanTickets(rules, tickets):
    validTickets = []
    invalidTickets = []
    allInvalidValues = []

    for ticket in tickets:
        invalidValues = validateTicket(rules, ticket)
        if len(invalidValues) == 0:
            validTickets.append(ticket)
        else:
            invalidTickets.append(ticket)
            allInvalidValues.extend(invalidValues)

    return validTickets, invalidTickets, allInvalidValues


#
# Sum the invalid Ticket numbers
#
def sumInvalidNumbers(tickets, positions):
    numSum = 0

    return numSum


#
# find the Field Positions based on rules and valid tickets
#
def findFieldPositions(rules, tickets):
    fieldPositions = {}

    # find all candidate field positions
    for field in rules.keys():
        positions = []

        for pos in range(len(tickets[0])):
            candidate = True
            for ticket in tickets:
                rangeCheck = False
                for start,end in rules[field]:
                    if start <= ticket[pos] and ticket[pos] <= end:
                        rangeCheck = True
                        break
                if not rangeCheck:
                    candidate = False
                    break
            if candidate:
                positions.append(pos)
            elif pos in positions:
                positions.remove(pos)

        fieldPositions[field] = positions
        #print(field, positions)

    # clean up duplicates
    change = True
    while change:
        change = False
        for field in fieldPositions:
            positions = fieldPositions[field]
            if isinstance(positions, list):
                if len(positions) == 1:
                    position = positions[0]
                    fieldPositions[field] = position
                    change = True
                    for p in fieldPositions.values():
                        if isinstance(p, list) and position in p:
                            p.remove(position)
            #print(field, positions)

    return fieldPositions


#
# Multiply all the departure fields
#
def mulDeparture(fieldPositions, myTicket):

    numSum = 1

    for fieldPosition in fieldPositions.keys():
        if fieldPosition.startswith("departure"):
            numSum *= myTicket[fieldPositions[fieldPosition]]

    return numSum


#
# Print the ticket
#
def printTicket(fieldPositions, myTicket):

    for field in fieldPositions:
        print(field,"=", myTicket[fieldPositions[field]])


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
    rules, myTicket, nearbyTickets, lines = loadData(filename)
    print("    Lines Read: ", len(lines))
    print("    Rules Read: ", len(rules))
    print("     My Ticket: ", len(myTicket))
    print("Nearby Tickets: ", len(nearbyTickets))
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    validTickets, invalidTickets, allInvalidValues = scanTickets(rules, nearbyTickets)
    print("     Valid Tickets: ", len(validTickets))
    print("   Invalid Tickets: ", len(invalidTickets))
    print("All Invalid Values: ", len(allInvalidValues))
    answer = sum(allInvalidValues)
    print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    fieldPositions = findFieldPositions(rules, validTickets)
    printTicket(fieldPositions,myTicket)
    answer = mulDeparture(fieldPositions, myTicket)
    print()
    print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
