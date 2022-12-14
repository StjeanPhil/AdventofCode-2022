import os,copy

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()
file = list(map(lambda line: line.strip(), file))
data = []
for line in file:
    row = []
    for c in line:
        row.append(c)
    data.append(row)


class Road:
    def __init__(self, map, latestpos, latestLetter, steps):
        self.map = map
        self.current = latestpos
        self.letter = latestLetter
        self.steps = steps

    def move(self):
        # check around for possible steps
        possiblesteps = []
        # right
        if (self.current[1]+1) < len(self.map[0]) and (self.map[self.current[0]][self.current[1]+1].isalpha()) :
            #print("hitright")
            possiblesteps.append([self.current[0], self.current[1]+1,">"])
            
        # left
        if self.current[1]-1 >= 0 and self.map[self.current[0]][self.current[1]-1].isalpha() :
            #print("hitleft")
            possiblesteps.append([self.current[0], self.current[1]-1,"<"])
            
        # down
        if self.current[0]+1 < len(self.map) and self.map[self.current[0]+1][self.current[1]].isalpha() :
            #print("hitdown")
            possiblesteps.append([self.current[0]+1, self.current[1],"|"])
            
        # up
        if self.current[0]-1 >= 0 and self.map[self.current[0]-1][self.current[1]].isalpha() :
            #print("hitup")
            possiblesteps.append([self.current[0]-1, self.current[1],"^"])
            

        # check posSteps for letter with ord() within 1 of current letter
        newRoads = []
       # print("exploring possible steps")
       # print(possiblesteps)
        for possible in possiblesteps:

            if ord(self.letter) == ord(self.map[possible[0]][possible[1]]) or \
                ord(self.letter) == ord(self.map[possible[0]][possible[1]])+1 or \
                ord(self.letter) == ord(self.map[possible[0]][possible[1]])-1 or \
                self.letter =="z" and self.map[possible[0]][possible[1]]=="E":
                

                latestLetter = self.map[possible[0]][possible[1]]
                steps = self.steps+1
                newMap= copy.deepcopy(self.map)
                newMap[possible[0]][possible[1]] =possible[2]
                newRoads.append(Road(newMap, possible, latestLetter, steps))

        #print("Creating new roads:", newRoads)
        return newRoads


def getPos(data):
    # Return the pos of the start and destination
    print("getPos: ")
    start = []
    end = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "S":
                start = [x, y]
            elif data[x][y] == "E":
                end = [x, y]
    print(start,end)
    return start, end


def solver(data):
    print("solver:")
    #Get the starting position and the ending position
    startPos, endPos = getPos(data)
    #Set ourselves at the start
    currPos = startPos
    #roads contains all the possible roads
    roads = [Road(data, currPos, "a", False)]
    #solved contains all the roads who arrived at destination
    solved = []
    #while there is roads to check:
    while roads:
        currRoad = roads.pop()
        newRoads = currRoad.move()
        for r in newRoads:
            #print(r.current)
            if r.map[endPos[0]][endPos[1]]=="E":
                #print("ROAD ADDED")
                roads.append(r)
            else:
                #print("Solved!")
                solved.append(r)

    print(solved)
    lowest = solved[0].steps
    for r in solved:
        print("steps:",r.steps)
        if lowest > r.steps:
            lowest = r.steps
    print("this the lowest:")
    return lowest


if __name__ == "__main__":
    print("Problem 1 :")
    print(solver(data))
