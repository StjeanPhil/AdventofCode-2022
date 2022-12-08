import os

class Directory:
    def __init__(self,name,parent=None):
        self.name=name
        self.parent=parent
        self.content=[]
        self.size=0
class Document:
    def __init__(self,size,name):
        self.size=int(size)
        self.name=name
        

def changeCurrentDir(command,dir):
    if command==".." and  dir.parent!= None:
            return dir.parent
    else:
        for doc in dir.content:
            if command == doc.name:
                return doc

def setDirTree(file):
    currDir=False
    for line in file:
        data=line.strip().split(" ")
        #Determine if its a command or result
        #Command
        if "$" in data:
            #Check what command was used
            if data[1]=="cd":
                if(not currDir):
                    currDir=Directory(data[2])
                else:
                    currDir =changeCurrentDir(data[2],currDir)
        #Result
        else:
                notadded=True
                #if the result isn't already in the currentDirectory
                for d in currDir.content:
                    if d.name == data[1]:
                        notadded=False
                #add the result  to the current directory
                if notadded:
                    #if the result is a directory
                    if data[0]=="dir":
                        currDir.content.append(Directory(data[1],currDir))
                    #if the result is a document
                    else:
                        currDir.content.append(Document(data[0],data[1]))
    while currDir.name != "/":
        currDir=changeCurrentDir("..",currDir)
    return currDir
    
def renderSize(dir):
    size=0
    for d in dir.content:
        if d.size==0:
            d.size=renderSize(d)
        size+=d.size
    return size


#Problem1
def sumSubX(directory,x):
    if directory.size<x:
        total=directory.size
    else:
        total=0

    for d in directory.content:
        if hasattr(d,"parent"):
            total+=sumSubX(d,x)
    return total

#Problem2
def closestSizeDir(dir,sizeGoal,closest):
    currclosest=closest
    for d in dir.content:
        if hasattr(d,"parent"):
            if currclosest>d.size>sizeGoal:
                currclosest=d.size
            currclosest=closestSizeDir(d,sizeGoal,currclosest)
    return currclosest
                
            
            



if __name__=="__main__":
    #Get the file
    file_name = "input.txt"
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    file = open(file_path, "r").readlines()
    #render the directory tree
    dirtree=setDirTree(file)
    dirtree.size=renderSize(dirtree)

    # sum of all directory under 100000 size
    print("Problem 1: ")
    print(sumSubX(dirtree,100000))

    print("Problem 2: ")    
    updateSize=30000000
    spaceAvailable=70000000-dirtree.size
    spaceNeeded=updateSize-spaceAvailable
    print(closestSizeDir(dirtree,spaceNeeded,dirtree.size))

  
