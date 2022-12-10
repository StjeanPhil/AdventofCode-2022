import os
from collections import deque

def getData():
    file_name = "input.txt"
    file_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), file_name)
    file = open(file_path, "r").readline()
    return file.strip()

def solver(data,length):
    queue=deque()
    for idx in range(len(data)):
        queue.append(data[idx])
        if len(set(queue))==length: return idx+1
        if len(queue)>=length: queue.popleft()

if __name__=="__main__":
    print("Problem 1: ",solver(getData(),4))
    print("Problem 2: ",solver(getData(),14))

