import os

# Get the file
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()

# SOLUTION DOES NOT WORK, HAVE TO IMPLEMENT A CHECK FOR ALREADY COUNTED TREES


def countline(line):
    nbTrees = 0
    currHeight = 0
    for tree in line:
        tree = int(tree)
        if 0 < tree > currHeight:
            nbTrees += 1
            currHeight = tree
    return nbTrees


def problem1(data):
    visibleTrees = 0
    # Get nbTrees visible by the sides
    for line in data:
        # RIGHT- LEFT LINE
        line = line.strip()
        visibleTrees += countline(line)
        # LEFT - RIGHT LINE
        visibleTrees += countline(line[::-1])

    # Change row for col
    verticalLines = [[]]*len(data[0].strip())
    for vertLine in range(len(data[0].strip())):
        for idx in range(len(data)):
            verticalLines[vertLine].append(data[idx].strip()[vertLine])

    for line in verticalLines:
        # TOP - DOWN LINE
        visibleTrees += countline(line)
        # DOWN - UP LINE
        visibleTrees += countline(line[:: -1])
    return visibleTrees


if __name__ == "__main__":
    print("Problem 1:")
    print(problem1(file))
