import os

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
        if self.map[self.current[0]][self.current[1]+1].isalpha() & (self.current[1]+1) < len(self.map[0]):
            possiblesteps.append([self.current[0], self.current[1]+1])
        # left
        if self.map[self.current[0]][self.current[1]-1].isalpha() & self.current[1]-1 >= 0:
            possiblesteps.append([self.current[0], self.current[1]-1])
        # down
        if self.map[self.current[0]+1][self.current[1]].isalpha() & self.current[0]+1 < len(self.map):
            possiblesteps.append([self.current[0]+1, self.current[1]])
        # up
        if self.map[self.current[0]-1][self.current[1]].isalpha() & self.current[0]-1 >= 0:
            possiblesteps.append([self.current[0]-1, self.current[1]])

        # check posSteps for letter with ord() within 1 of current letter
        newRoads = []
        for possible in possiblesteps:

            if ord(self.letter) == ord(self.map[possible[0]][possible[1]]) or \
                    ord(self.letter) == ord(self.map[possible[0]][possible[1]])+1 or \
                    ord(self.letter) == ord(self.map[possible[0]][possible[1]])-1:
                newMap = self.map
                newMap[possible[0]][possible[1]] = "#"
                latestLetter = self.map[possible[0]][possible[1]]
                steps = self.steps+1
                newRoads.append(Road(newMap, possible, latestLetter, steps))
        print("Creating new roads:", newRoads)
        return newRoads


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


def solver(data):
    startPos, endPos = getPos(data)
    currPos = startPos
    roads = [Road(data, currPos, "a", False)]
    solved = []

    while roads:
        print("check roads: ", roads)
        currRoad = roads.pop()
        newRoads = currRoad.move()
        for r in newRoads:
            if r.current[0] != endPos[0] or r.current[1] != endPos[1]:
                roads.append(r)
            else:
                solved.append(r)
        print("post while ", roads)

    print(solved)
    lowest = solved[0].steps
    for r in solved:
        if lowest > r.steps:
            lowest = r.steps
    return lowest


if __name__ == "__main__":
    print("Problem 1 :")
    print(solver(data))
