import os
file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()
file = [d.strip() for d in open(file_path, "r").readlines() if d != "\n"]

def getPosFromString(posString):
    pos=posString.split(",")
    x=int(pos[0].split("=")[1])
    y=int(pos[1].split("=")[1])
    return (x,y)

def parseInput(file):
    sensors,beacons=[],[]
    for line in file:
        sensor,beacon=line.split(":")
        sensor=getPosFromString(sensor.strip("Sensor at "))
        beacon=getPosFromString(beacon.strip(" closest beacon is at "))
        sensors.append(sensor)
        beacons.append(beacon) 
        #print(sensor,beacon)      
    return (sensors,beacons)


def getDistances(sensors,beacons):
    distances=[]
    print("sensor - beacon - distance")
    for pos1,pos2 in zip(sensors,beacons):
        distances.append(abs(pos2[0]-pos1[0])+abs(pos2[1]-pos1[1]))
        print(pos1,pos2,distances[-1])
    return distances

def solver(file,row):
    sensors,beacons = parseInput(file)
    distances=getDistances(sensors,beacons)
    intervals=[] #list of interval of pos on row
    #for each sensor, check if it's range touches the row specified in params
    for sensor,distance in zip(sensors,distances):
        if abs(sensor[1] - row) < distance:
            over=abs(distance - abs(sensor[1] - row))
            #the difference between the max range of sensor and the row equals to the range in the row
            intervals.append([sensor[0]-over,sensor[0]+over])
    #add all number included in intervals to the set
    notHere=set()
    for inter in intervals:
        start,end=inter[0],inter[1]
        for i in range(start,end):
            notHere.add(i)
    #return the amount of blocked positions on row specified in params
    return len(notHere)

def solverpart2(file,maxSize):
    sensors,beacons = parseInput(file)
    distances=getDistances(sensors,beacons)
    for row in range(maxSize+1):
            
        intervals=[] #list of interval of pos on row
        #for each sensor, check if it's range touches the row specified in params
        for sensor,distance in zip(sensors,distances):
            if abs(sensor[1] - row) < distance:
                over=abs(distance - abs(sensor[1] - row))
                #the difference between the max range of sensor and the row equals to the range in the row
                intervals.append([sensor[0]-over,sensor[0]+over])
        #add all number included in intervals to the set
        notHere=set()
        for inter in intervals:
            start,end=inter[0],inter[1]
            for i in range(start,end):
                notHere.add(i)
        #return the amount of blocked positions on row specified in params
        if len(notHere)==1:
            notHere=list(notHere)
            x,y = notHere[0],row
            break
    return (x*maxSize)+y




if __name__ == "__main__":
    print("Problem 1 :")
    print(solver(file,2_000_000))
    print("Problem 2 :")
    print(solverpart2(file,4_000_000))
