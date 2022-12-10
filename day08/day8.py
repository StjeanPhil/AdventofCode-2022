import os

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()

#Strip the file
for x in range(len(file)):
    file[x]=file[x].strip()  

def prob1(file):        
    #Create the right size starting checklist
    checklist=[]
    for x in range(len(file)):
        row=[]
        for y in range(len(file[0])):
            row.append(False)
        checklist.append(row)        

    #Left-right
    for x in range(len(file)):
        currHeight=-1
        for y in range(len(file[0])):
            height=int(file[x][y])
            if height>currHeight:
                currHeight=int(file[x][y])
                checklist[x][y]=True
    #right-left
    for x in range(len(file)):
        currHeight=-1
        row=[]
        for y in range (len(file[0])):
            height=int(file[x][-(y+1)])
            if(height>currHeight):
                currHeight=height
                row.append(True)
            else:
                row.append(False)
        row.reverse()
        for idx in range(len(row)):
            if row[idx]:
                checklist[x][idx]=True
    #Top-down
    for y in range(len(file[0])):
        currHeight=-1
        row=[]
        for x in range (len(file)):
            height=int(file[x][y])
            if(height>currHeight):
                currHeight=height
                row.append(True)
            else:
                row.append(False)

        for idx in range(len(row)):
            if row[idx]:
                checklist[idx][y]=True
    #Down-Top            
    for y in range(len(file[0])):
        currHeight=-1
        row=[]
        for x in range (len(file)):
            height=int(file[-(x+1)][y])
            if(height>currHeight):
                currHeight=height
                row.append(True)
            else:
                row.append(False)
        row.reverse()
        for idx in range(len(row)):
            if row[idx]:
                checklist[idx][y]=True
    #Counting the visible trees
    nbTrees= 0
    for line in checklist:
        for tree in line:
            if tree : nbTrees+=1

    print("Problem 1: ",nbTrees)


def prob2(file):
    topscore=0
    for x in range(len(file)):
        for y in range(len(file[0])):
            score=getScore(x,y,file)
            if topscore<score:
                topscore=score
    print ("Problem 2: ",topscore)

def getScore(ligne,col,data):

    rightScore=0
    leftScore=0
    upScore=0
    downScore=0

    currHeight=int(data[ligne][col])
    #print("down encounter:")

    for x in range(1,len(data)-ligne):
        height=int(data[ligne+x][col])
       # print(height)
        downScore+=1
        if(height>=currHeight):
            break
   # print("up encounter:")
    for x in range(1 ,ligne+1):
        height=int(data[ligne-x][col])
       # print(height)
        upScore+=1
        if(height>=currHeight):
            break
    #print("right encounter:")
    for y in range(1,len(data[0])-col):
        height=int(data[ligne][col+y])
       # print(height)
        rightScore+=1
        if(height>=currHeight):
            break
   # print("left encounter:")
    for y in range(1,col+1):
        height=int(data[ligne][col-y])
       # print(height)
        leftScore+=1
        if(height>=currHeight):break
    
    return (rightScore*leftScore*upScore*downScore)


if __name__=="__main__":
    prob1(file)
    prob2(file)