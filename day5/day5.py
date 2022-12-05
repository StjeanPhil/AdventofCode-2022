import os

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
# file = open(file_path, "r")


def initValues(file):
    data = file
    newstacks = [[] for idx in range(0, 9)]
    nums = []
    for line in data.readlines():
        # Load the starting stacks
        if "[" in line:
            for idx in range(0, 9):
                if line[1+(idx*4)].isalpha():
                    newstacks[idx].append(line[1+idx*4])
        elif "move" in line:
            # Get the numbers for the moves:
            #   0: nb of letter to transfer
            #   1: origin stack
            #   2: destination stack
            nums.append([(int(x)-1) for x in line.split() if x.isdigit()])
    # Reverse the starting stacks
    for idx in range(len(newstacks)):
        newstacks[idx].reverse()
    return newstacks, nums


def printSolution(stack):
    solvedStack = stack
    letters = ""
    for idx in range(len(solvedStack)):
        letters += solvedStack[idx][len(solvedStack[idx])-1]
    print(letters)


def moveP1(stacks, nums):
    newStack = stacks
    # Move crate from origin stack to destination stack one at a time
    while nums[0] >= 0 and newStack[nums[1]]:
        newStack[nums[2]].append(newStack[nums[1]].pop())
        nums[0] -= 1
    return newStack


def moveP2(stacks, nums):
    # Move crate from origin stack to destination stack one at a time
    tempStack = []
    # print(stacks[nums[1]])
    while nums[0] >= 0 and stacks[nums[1]]:
        tempStack.append(stacks[nums[1]].pop())
        nums[0] -= 1
    # print(tempStack)
    while tempStack:
        stacks[nums[2]] += tempStack.pop()
    return stacks


def problemSolver(probNb):
    file = open(file_path, "r")

    print("Problem ", probNb, " :")
    stacks, nums = initValues(file)
    for num in nums:
        if probNb == "1":
            stacks = moveP1(stacks, num)
        elif probNb == "2":
            stacks = moveP2(stacks, num)
    printSolution(stacks)


problemSolver("1")
problemSolver("2")
