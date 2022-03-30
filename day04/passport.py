#
# Adavent of Code Template
#
import sys
import re

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


fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

#
# Load the file into a data array
#
def loadData(filename):

    lines = []
    passports = []
    passport = {}
    passports.append(passport)

    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)
        if len(line) == 0:
            passport = {}
            passports.append(passport)
        else:
            parts = line.split(" ")
            for part in parts:
                field, value = part.split(":")
                passport[field] = value

    f.close()

    return passports, lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# count valid passports by only checking presence of fields
#
def countValidFieldPassports(passports):
    validPassports = 0

    for passport in passports:
        if len(list(set(requiredFields) - set(passport.keys()))) == 0:
            validPassports += 1

    return validPassports


#
# Check the data value in the field to see if it is valid
#
def validData(field, value):
    validValue = False

    if field == "byr":
        # Birth Year
        if value.isnumeric() and len(value) == 4:
            v = int(value)
            if 1920 <= v and v <= 2002:
                validValue = True

    elif field == "iyr":
        # Issue Year
        if value.isnumeric() and len(value) == 4:
            v = int(value)
            if 2010 <= v and v <= 2020:
                validValue = True

    elif field == "eyr":
        # Expiration Year
        if value.isnumeric() and len(value) == 4:
            v = int(value)
            if 2020 <= v and v <= 2030:
                validValue = True

    elif field == "hgt":
        # Height
        iscm = value.endswith("cm")
        isin = value.endswith("in")
        if iscm or isin:
            v = int(value[:-2])
            if (iscm and 150 <= v and v <= 193) or (isin and 59 <= v and v <= 76):
                validValue = True

    elif field == "hcl":
        # Hair Color
        if len(value) == 7 and value[0] == "#":
            validValue = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)

    elif field == "ecl":
        # Eye Color
        validValue = value in ["amb","blu","brn","gry","grn","hzl","oth"]

    elif field == "pid":
        # Passport ID
        if value.isnumeric() and len(value) == 9:
            validValue = True

    elif field == "cid":
        # Country ID
        validValue = True

    return validValue


#
# count valid passports by checking fields and data values
#
def countValidDataPassports(passports):
    validPassports = 0

    for passport in passports:
        validPassport = True
        for field in requiredFields:
            if field not in passport.keys():
                validPassport = False
                break
            if not validData(field, passport[field]):
                validPassport = False
                break

        if validPassport: validPassports += 1

    return validPassports


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
    passports, lines = loadData(filename)
    print(" Lines Read: ", len(lines))
    print()
    #printLines(lines)

    # Do Part 1 work
    print()
    answer = countValidFieldPassports(passports)
    print()
    print("{}Valid Field Passports: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    print()
    answer = countValidDataPassports(passports)
    print()
    print("{}Valid Data Passports: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


if __name__ == "__main__":
    main()
