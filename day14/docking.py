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

BITS = 36

#
# Load the file into a data array
#
def loadData(filename):

    instructions = []

    f = open(filename)
    for line in f:
        line = line.strip()
        part1, part2 = line.split("=")
        part1 = part1.strip()
        part2 = part2.strip()
        if part1 == "mask":
            instruction = part1
            value = part2
            addr = 0
        else:
            instruction, addr = part1.split("[")
            value = int(part2)
            addr = int(addr[:-1])
        instructions.append((instruction, addr, value))

    f.close()

    return instructions


#
# Print Instructions
#
def printInstructions(instructions):

    for instruction in instructions:
      print(instruction)


#
# Apply Mask to the value
#
def maskValue(mask, value):
    result = value

    zeros = int(mask.replace("X","1"),2)
    ones = int(mask.replace("X","0"),2)

    result &= zeros
    result |= ones

    #print("  mask", "{:s}".format(mask))
    #print(" zeros", "{:0>36b}".format(zeros))
    #print("  ones", "{:0>36b}".format(ones))
    #print(" value", "{:0>36b}".format(value))
    #print("result", "{:0>36b}".format(result))

    return result


#
# Apply the instructions to the memory
#
def applyInstructions(instructions):

    memory = {}

    mask = "X" * BITS
    for instruction, addr, value in instructions:
        if instruction == "mask":
            mask = value
        else:
            memory[addr] = maskValue(mask,value)

    return memory


#
# Apply Mask to the address
#
def maskAddress(mask, address):

    #print()
    #print("M",mask)
    #print("A","{:0>36b}".format(address), address)
    floating = []

    for pos in range(BITS):
        if mask[pos] == "0":
            continue
        elif mask[pos] == "1":
            address |= 2 ** (BITS-pos-1)
        else:
            if address & 2**(BITS-pos-1) != 0:
                address -= 2 ** (BITS-pos-1)
            floating.append(BITS-pos-1)

    #print(floating)
    return floatingAddresses(floating, address)


#
# generate all the floating addresses
#
def floatingAddresses(floating, address):

    pos = floating[0]
    #print("pos",pos)

    if len(floating) > 1:
        for zeroAddr in floatingAddresses(floating[1:], address):
            #print("0","{:0>36b}".format(zeroAddr), zeroAddr)
            yield zeroAddr
    else:
        yield address

    address |= 2 ** pos
    if len(floating) > 1:
        for oneAddr in floatingAddresses(floating[1:], address):
            #print("1","{:0>36b}".format(oneAddr), oneAddr)
            yield oneAddr
    else:
        yield address


#
# Apply the instructions to the memory using V2 logic
#
def applyInstructions2(instructions):

    memory = {}

    mask = "0" * BITS
    for instruction, addr, value in instructions:
        if instruction == "mask":
            mask = value
        else:
            addresses = maskAddress(mask,addr)
            #print(addresses)
            for address in addresses:
                memory[address] = value

    return memory


#
# sum all memory locations
#
def sumMemory(memory):

    return sum(memory.values())


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
    instructions = loadData(filename)
    print("Instructions Read: ", len(instructions))
    print()
    #printInstructions(instructions)

    # Do Part 1 work
    print()
    memory = applyInstructions(instructions)
    answer = sumMemory(memory)
    print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    memory = applyInstructions2(instructions)
    answer = sumMemory(memory)
    print()
    print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
