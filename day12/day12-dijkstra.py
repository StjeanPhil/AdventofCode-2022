import os
from collections import deque

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()
file = list(map(lambda line: line.strip(), file))


class Node:
    def __init__(self, letter,pos):
        self.height=ord(letter)
        self.pos=pos
        self.cost=999999999


def getPos(data):
    # Return the pos of the start and destination

    start = []
    end = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "S":
                start = [x, y]
            elif data[x][y] == "E":
                end = [x, y]

    return start, end

def convert2Node(file):
    #Transform the file into a 2d aray of nodes
    data = []
    for x in range(len(file)):
        row = []
        for y in range(len(file[x])):
            row.append(Node(file[x][y],[x,y]))
        data.append(row)
    return data

def getPossible(pos,data):
    #make sure the 4 possible pos are allowed
    possible=[]
    if pos[1]+1<len(data[pos[0]]):
        possible.append([pos[0],pos[1]+1])
    if pos[1]-1>=0:
        possible.append([pos[0],pos[1]-1])
    if pos[0]+1<len(data):
        possible.append([pos[0]+1,pos[1]])
    if pos[0]-1>=0:
        possible.append([pos[0]-1,pos[1]])
    return possible
            

def solver(file,prob):

    #Get the starting position and the ending position
    startPos, endPos = getPos(file)
    data=convert2Node(file)
    #List of not visited nodes
    notVisited=[]
    for row in data:
        for n in row:
            notVisited.append(n)
    #Put working values in the start and end nodes
    data[endPos[0]][endPos[1]].height=ord("z")
    data[startPos[0]][startPos[1]].cost=0
    data[startPos[0]][startPos[1]].height=ord("a")
    #sort the notvisited list so the lower cost gets pop() first
    notVisited = sorted(notVisited,key=lambda x: x.cost,reverse=True)

    #while there is still nodes to visit
    while notVisited:
        #grab the closest node not visited and remove it from the notvisited stack
        n=notVisited.pop()
        pos=n.pos
        #get the next possible nodes into the possible list
        possible=getPossible(pos,data)
        #
        for nextPos in possible:
            next=data[nextPos[0]][nextPos[1]]
            #Check if the possible next node height is max 1 off the current note
            if n.height+1>=next.height: 
                # check if we can offer a better cost
                if next.cost>(n.cost+1):
                    #print(data[nextPos[0]][nextPos[1]].height)
                    #update the cost
                    next.cost=n.cost+1
                    if prob==2 and next.height==(ord("a")):
                        next.cost=0
                    #Re-sort the notvisited by cost to account for the new cost of next
                    notVisited =sorted(notVisited,key=lambda x: x.cost,reverse=True)
                #if we reach end, quit
                if next.pos==endPos:

                    break

    
    return data[endPos[0]][endPos[1]].cost




if __name__ == "__main__":
    print("Problem 1 :")
    print(solver(file,1))
    print("Problem 2 :")
    print(solver(file,2))