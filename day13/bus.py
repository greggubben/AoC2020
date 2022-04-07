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

    departTime = 0
    buses = []

    f = open(filename)
    for line in f:
        line = line.strip()
        if departTime == 0:
            departTime = int(line)
        else:
            buses = line.split(",")

    f.close()

    return departTime, buses


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Find the earliest bus to depart
#
def findEarliestBus(departTime, buses):
    lowestWait = departTime
    earliestBusID = 0

    for b in buses:
        if b != "x":
            busID = int(b)
            wait = busID - (departTime % busID)
            if wait < lowestWait:
                lowestWait = wait
                earliestBusID = busID

    return earliestBusID, lowestWait


#
# Find the earliest timestamp when buses arrive at offsets match positions
# Use Chinese Remainder Theorem
#
# bi = remainder
# ni = mod
# N = all mods multiplied together
# Ni = N/ni - multiple all mods except this one
# xi = inverse of Ni or Ni * xi = 1 (mod ni)
# 
#
def findOrderedOffsetTime(buses):
    print("buses", buses)
    
    mods = []           # (bi,ni)
    
    busPos = 0
    N = 1
    for offset, b in enumerate(buses):
        if b != "x":
            busID = int(b)
            mods.append((busID-(busPos%busID), busID))
            N *= busID
        busPos += 1

    table = []
    xo = 0
    for (bi, ni) in mods:
        Ni = N//ni
        xi = inverseNi(Ni,ni)
        biNixi = bi * Ni * xi
        table.append((bi, ni, Ni, xi, biNixi))
        xo += biNixi
    x = xo % N

    print("mods (bi, ni)", mods)
    print("table (bi, ni, Ni, xi, biNixi)", table)
    print()
    print("{:>16}   {:>3}    {:>3}    {:>3}    | {:>3} | {:>15} | {:>3} | {:>18} | {:>3}".format("", "", "", "", "bi", "Ni", "xi", "biNixi", "mod"))
    print("{:>16}   {:>3}    {:>3}    {:>3}    +-{:>3}-+-{:>15}-+-{:>3}-+-{:>18}-+".format("", "", "", "", "-"*3, "-"*15, "-"*3, "-"*18))
    for (bi, ni, Ni, xi, biNixi) in table:
        print("{:>16} = {:>3}(mod{:>3}) = {:>3}    | {:>3} | {:>15} | {:>3} | {:>18} | {:>3}".format(x, bi, ni, x % ni, bi, Ni, xi, biNixi, biNixi % ni))
    print("{:>16}   {:>3}    {:>3}    {:>3}    +-{:>3}-+-{:>15}-+-{:>3}-+-{:>18}-+".format("", "", "", "", "-"*3, "-"*15, "-"*3, "-"*18))
    print("{:>16}   {:>3}    {:>3}    {:>3}      {:>3} = {:>15}   {:>3} | {:>18} |".format("", "", "", "", "N", N, "", xo))

    return x


#
# Find the inverse of Ni
#
def inverseNi(Ni, n):

    c = Ni % n
    for xi in range(1,n):
        if (xi * c) % n == 1:
            return xi


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
    departTime, buses = loadData(filename)
    busIDs = len(buses) - buses.count("x")
    print("Depart Time: ", departTime)
    print("      Buses: ", len(buses))
    print("    Bus IDs: ", busIDs)
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    busID, waitTime = findEarliestBus(departTime, buses)
    answer = busID * waitTime
    print()
    print("Take Bus:", busID, " with wait of",waitTime)
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = findOrderedOffsetTime(buses)
    print()
    print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
