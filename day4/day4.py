import os
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()

# theres is 2 sections per line
# section seperated by ","
# each section contain min and max of player
# return total nb of occurence of player min-max being contained in the other player

# Counters
total = 0
partial = 0

for line in file:
    # Seperate the elfs
    elf1, elf2 = line.strip().split(",")
    # Access their min and max
    elf1min, elf1max = elf1.split("-")
    elf2min, elf2max = elf2.split("-")
    # Convert string to int
    elf1min = int(elf1min)
    elf1max = int(elf1max)
    elf2min = int(elf2min)
    elf2max = int(elf2max)
    # Compare elfs
    # Total Overlap:
    if (elf1min <= elf2min and elf1max >= elf2max):
        total += 1
    elif (elf1min >= elf2min and elf1max <= elf2max):
        total += 1
    # Partial Overlap:
    if (elf1min >= elf2min and elf1min <= elf2max):
        partial += 1
    elif (elf1max >= elf2min and elf1max <= elf2max):
        partial += 1
    elif (elf2max >= elf1min and elf2max <= elf1max):
        partial += 1


# Print answer
print("Problem 1 :", total)

print("Problem 2 :", partial)
