import os
import itertools

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()
file = [d.strip() for d in open(file_path, "r").readlines() if d != "\n"]


def getPacketsPair(file):
    packets = []
    for idx in range(0, len(file), 2):
        pair = []
        pair.append(eval(file[idx]))
        pair.append(eval(file[idx+1]))
        packets.append(pair)
    return packets


def isRightOrder(left, right):
    #print("Compare ", left, " vs ", right)
    # Compare if both are number
    if isinstance(left, int) and isinstance(right, int):
        if left < right:  # Right
            return True
        elif left > right:  # Wrong
            return False
    elif isinstance(left, int) and not isinstance(right, int):
        return isRightOrder([left], right)
    elif not isinstance(left, int) and isinstance(right, int):
        return isRightOrder(left, [right])
    else:
        # if both are list, check left item one at a time
        # itertools.zip_longest make sure both list are the same size by adding "None" elements to the smallest list
        for val in itertools.zip_longest(left, right):
            if val[0] is None:
                return True
            if val[1] is None:
                return False
            ans = isRightOrder(val[0], val[1])
            if ans is not None:
                return ans


def solverPart1(file):
    packets = getPacketsPair(file)
    idx = 1
    total = 0
    for pair in packets:
        left = pair[0]
        right = pair[1]
        if isRightOrder(left, right):
            total += idx
        idx += 1
    return total


def solverPart2(file):
    packets = []
    # get packets outside of their pair
    for line in file:
        packets.append(eval(line))
    # add the two packets to look for
    packets.append([[2]])
    packets.append([[6]])
    # order the packets list by comparing all sequential values
    # if a comparaison result in a switch, the list was not inOrder. update inOrder
    inOrder = False
    while not inOrder:
        inOrder = True
        for idx in range(len(packets)-1):
            if not isRightOrder(packets[idx], packets[idx+1]):
                inOrder = False
                packets[idx], packets[idx+1] = packets[idx+1], packets[idx]
    # Get the indexes of the packets we added
    reponse = [1, 1]
    for idx in range(len(packets)):
        if packets[idx] == [[2]]:
            reponse[0] += idx
        if packets[idx] == [[6]]:
            reponse[1] += idx
    return reponse[0]*reponse[1]


if __name__ == "__main__":
    print("Problem 1 :")
    print(solverPart1(file))

    print("Problem 2 :")
    print(solverPart2(file))
