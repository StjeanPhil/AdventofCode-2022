import os

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()

class Knot:
    def __init__(self,x,y,parent):
        self.parent=parent
        self.x=x
        self.y=y
        self.child=None
    #Render rope movement and return position of the last knot
    def move(self):
        #Si self et son parent sont sur une meme ligne/col
        if self.x == self.parent.x or self.y == self.parent.y:
            #Si il y a un ecart de 2+ case
            if abs(self.x-self.parent.x)>=2:
                #Deplacer le self dans la bonne direction
                if self.x<self.parent.x:
                    self.x+=1
                else:
                    self.x-=1
            if abs(self.y-self.parent.y)>=2:
                if self.y<self.parent.y:
                    self.y+=1
                else:
                    self.y-=1
        #Si self et parent sont en diagonal
        else:
            if abs(self.x-self.parent.x)>=2:
                #Deplacer le self dans la bonne direction
                if self.x<self.parent.x:
                    self.x+=1
                else:
                    self.x-=1
                if self.y<self.parent.y:
                    self.y+=1
                else:
                    self.y-=1

            if abs(self.y-self.parent.y)>=2:
                if self.x<self.parent.x:
                    self.x+=1
                else:
                    self.x-=1
                if self.y<self.parent.y:
                    self.y+=1
                else:
                    self.y-=1
        #Return the pos of the last knot of the rope
        if self.child:
            pos = self.child.move()
        else:
            pos= (str(self.x)+","+str(self.y))
        return pos

def solver(moves,rope):
    #tracker for the head and second knot of the rope
    head=rope
    secondKnot= head.child
    #Keep track of the position of the last knot of the rope
    posVisited=[]
    #Execute Moves
    for move in moves:
        direction,steps=move.strip().split()
        steps=int(steps)
        if(direction=="R"):            
            for step in range(steps):
                head.x+=1
                posVisited.append(secondKnot.move())
        elif direction=="L":
            for step in range(steps):
                head.x-=1
                posVisited.append(secondKnot.move())
        elif direction=="U":
            for step in range(steps):
                head.y-=1
                posVisited.append(secondKnot.move())
        elif direction=="D":
            for step in range(steps):
                head.y+=1
                posVisited.append(secondKnot.move())  
    #after removing duplicates, Return the number of positions visited 
    return (len(set(posVisited)))

def createRope(length):
    head=Knot(0,0,None)
    currKnot=head
    for i in range(length-1):
        currKnot.child=Knot(0,0,currKnot)
        currKnot=currKnot.child
    return head

if __name__=="__main__":

    print("Problem 1 :",solver(file,createRope(2)))
    print("Problem 2: ",solver(file,createRope(10)))