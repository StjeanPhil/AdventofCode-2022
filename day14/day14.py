import os
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()
file = [d.strip() for d in open(file_path, "r").readlines() if d != "\n"]

def getPaths(data):
    #Convert the file into paths: list of coords
    paths=[]
    for line in data:
        #split stringPath into different coord
        positions=line.split(" -> ")
        for idx in range(len(positions)):
            #split the coord into 2 number
            positions[idx]=positions[idx].split(",")
            for index in range(len(positions[idx])):
                #Convert coord from string to int
                positions[idx][index]=int(positions[idx][index])
        paths.append(positions)
    return paths

def getBlockedPos(paths):
    blocked=set()
    for path in paths:
        for idx in range(len(path)):
            #Add current pos to blockedPos
            blocked.add((path[idx][0],path[idx][1]))
            #If it is not the last pos in the path
            if idx+1<len(path):
                currPos=path[idx]
                nextPos=path[idx+1]
                #add all pos of the path to blocked pos
                if currPos[0] != nextPos[0]:
                    if(currPos[0]<nextPos[0]):
                        for x in range(currPos[0]+1,nextPos[0]):
                            blocked.add((x,currPos[1]))
                    else:
                        for x in range(nextPos[0],currPos[0]):
                            blocked.add((x,currPos[1]))

                elif currPos[1] != nextPos[1]:
                    if currPos[1]<nextPos[1]:
                        for y in range(currPos[1]+1,nextPos[1]):
                            blocked.add((currPos[0],y))
                    else:
                        for y in range(nextPos[1],currPos[1]):
                            blocked.add((currPos[0],y))
    return blocked

def getGrid(blocked):
    maxDepth=0
    maxWidth=0
    for coord in blocked:
        if coord[0]>maxWidth:
            maxWidth=coord[0] 
        if coord[1]>maxDepth:
            maxDepth=coord[1]
    grid=[]       
    for x in range(maxWidth+1):
        row=[]
        for y in range(maxDepth+1):
            row.append(False)
        grid.append(row)
    for coord in blocked:
        grid[coord[0]][coord[1]]=True
    return grid
    
def getVoidLevel(blocked):
    lowest=0
    for coord in blocked:
        if coord[1]>lowest:
            lowest=coord[1]
    return lowest

def addSandBlock(blocked,floor,prob):
    sandBlock=[500,0]
    placed=False
    while not placed:
        if not (sandBlock[0],sandBlock[1]+1) in blocked:
            sandBlock[1]+=1
        elif not (sandBlock[0]-1,sandBlock[1]+1) in blocked:
            sandBlock[0]-=1
            sandBlock[1]+=1
        elif not (sandBlock[0]+1,sandBlock[1]+1) in blocked:
            sandBlock[0]+=1
            sandBlock[1]+=1
        else:
            placed=True
        if sandBlock[1]==floor:
            if prob==1:
                return [],sandBlock
            else:
                placed=True
    blocked.add((sandBlock[0],sandBlock[1]))
    return blocked,sandBlock

    

def solver(file):
    blockedPos=getBlockedPos(getPaths(file))    #all the position blocked by rocks on all the paths
    #the lowest rock
    void=getVoidLevel(blockedPos)
    abyssReached=False
    nbSandBlock=0

    while not abyssReached:
        #print("Dropping sand")
        grid,lastSandPos = addSandBlock(blockedPos,void,prob=1)
        if lastSandPos[1]==void: abyssReached=True
        if not abyssReached: nbSandBlock+=1
    return nbSandBlock

def solverpart2(file):
    blockedPos=getBlockedPos(getPaths(file))    #all the position blocked by rocks on all the pathss
    floor=getVoidLevel(blockedPos)+1    #Part 2 includes an infinite floor 2 below the lowest rock

    sandSpawner=[500,0]
    nbSandBlock=0
    lastSandPos=[]

    while sandSpawner!= lastSandPos:
        blockedPos,lastSandPos=addSandBlock(blockedPos,floor,prob=2)
        nbSandBlock+=1
    
    return nbSandBlock






if __name__ == "__main__":
    print("Problem 1 :")
    print(solver(file))

    print("Problem 2 :")
    print(solverpart2(file))
