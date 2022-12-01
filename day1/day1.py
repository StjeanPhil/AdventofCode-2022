# About the input:
# Each line is a caloric counter of a item of food
# Each block is the food inventory of a single elf
# Blocks are seperated by an empty line

# Problem 1: return highest total calories of an inventory
# Problem 2: reutrn the sum of the 3 highes total calories of an inventory

file = open("input.txt", "r")

thirdSum, secondSum, firstSum, currentSum = 0, 0, 0, 0

for line in file:
    if (line.strip()):
        currentSum += int(line)
    else:
        if currentSum > firstSum:
            thirdSum = secondSum
            secondSum = firstSum
            firstSum = currentSum
        elif currentSum > secondSum:
            thirdSum = secondSum
            secondSum = currentSum
        elif currentSum > thirdSum:
            thirdSum = currentSum
        currentSum = 0

topSums = firstSum+secondSum+thirdSum
print("Solution 1: ", firstSum)
print("Solution 2: ", topSums)
