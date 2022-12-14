import os
from collections import deque

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()

file = list(map(lambda line: line.strip(), file))
def getDataPairs(data):
    pairs=[[]]
    idx=0
    for line in data:
        if line!="":
            pairs[idx].append(line)
        else:
            pairs.append([])
            idx+=1
    return pairs

def solver(data):
    left,right=[],[]
    total=0
    pairs=getDataPairs(data)
    for packet in pairs:
        left=packet[0]
        right=packet[1]
        print(packet)
    




if __name__ == "__main__":
    print("Problem 1 :")
    solver(file)