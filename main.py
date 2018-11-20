# Updated Animation Starter Code

from tkinter import *
import random

### map code ###

class Builder(object):
    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.numSpawners = random.randint(2,4)
        self.spawners = []
        
    def addSpawners(self):
        for i in range(self.numSpawners):
            dist = random.randint(5,10)
            spawnDirections = ["Up","Right","Down","Left"]
            direction = spawnDirections[i]
            if direction == "Up":
                self.spawners.append(Spawner(self.x0,self.y0-30,self.x1,self.y0,"Up",dist))
            elif direction == "Right":
                self.spawners.append(Spawner(self.x1,self.y0,self.x1+30,self.y1,"Right",dist))
            elif direction == "Down":
                self.spawners.append(Spawner(self.x0,self.y1,self.x1,self.y1+30,"Down",dist))
            elif direction == "Left":
                self.spawners.append(Spawner(self.x0-30,self.y0,self.x0,self.y1,"Left",dist))
        
    def drawBuilder(self,canvas):
        canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill="white",outline="white")
        for i in range(self.numSpawners):
            if i == 0:
                canvas.create_rectangle(self.x0,self.y0-30,self.x1,self.y0,outline="white",fill="white")
            if i == 1:
                canvas.create_rectangle(self.x1,self.y0,self.x1+30,self.y1,outline="white",fill="white")
            if i == 2:
                canvas.create_rectangle(self.x0,self.y1,self.x1,self.y1+30,outline="white",fill="white")
            if i == 3:
                canvas.create_rectangle(self.x0-30,self.y0,self.x0,self.y1,outline="white",fill="white")
        
class Spawner(Builder):
    directions = ["Right","Left","Up","Down"]
    def __init__(self,x0,y0,x1,y1,direction,distance):
        super().__init__(x0,y0,x1,y1)
        self.direction = direction
        self.distance = distance
        self.distTraveled = 0
        
    def drawSpawner(self,canvas):
        canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill="white",outline="white")
    
    def moveSpawner(self):
        if self.direction == "Up":
            self.y0 -= 30
            self.y1 -= 30
        elif self.direction == "Right":
            self.x0 += 30
            self.x1 += 30
        elif self.direction == "Down":
            self.y0 += 30
            self.y1 += 30
        elif self.direction == "Left":
            self.x0 -= 30
            self.x1 -= 30
    
    def turnSpawner(self):
        if self.direction == "Up" or self.direction == "Down":
            self.direction = random.choice(["Right","Left"])
        elif self.direction == "Right" or self.direction == "Left":
            self.direction = random.choice(["Up","Down"])
            
### dot code ###

class Dot(object):
    def __init__(self,cx,cy):
        self.cx = cx
        self.cy = cy
        self.r = 2
        
    def drawDot(self,canvas):
        x0 = self.cx - 2
        y0 = self.cy - 2
        x1 = self.cx + 2
        y1 = self.cy + 2
        canvas.create_oval(x0,y0,x1,y1,fill="green")

### pacman code ###

class Pacman(object):
    def __init__(self,cx,cy):
        self.cx = cx
        self.cy = cy
        self.speed = 10
        self.direction = None
        self.r = 15
        self.row = cx//30
        self.col = cy//30
        
    def draw(self,canvas):
        x0 = self.cx - self.r
        y0 = self.cy - self.r
        x1 = self.cx + self.r
        y1 = self.cy + self.r
        canvas.create_oval(x0,y0,x1,y1,fill="yellow")
        
    def move(self):
        if self.direction != None:
            if self.direction == "Right":
                self.cx += self.speed
                self.col += (1/3)
            elif self.direction == "Left":
                self.cx -= self.speed
                self.col -= (1/3)
            elif self.direction == "Up":
                self.cy -= self.speed
                self.row -= (1/3)
            elif self.direction == "Down":
                self.cy += self.speed
                self.row += (1/3)
    
    def collidesWithWall(self,other):
        leftEdge = self.cx - self.r
        rightEdge = self.cx + self.r
        topEdge = self.cy - self.r
        bottomEdge = self.cy + self.r
        if (not isinstance(other,Wall)):
            return False
        else:
            pass
            
    def addBuilder(self):
        builderR = 15
        width = 750
        height = 600
        numRows = width//30
        numCols = height//30
        builderRow = random.randint(0,numRows)
        builderCol = random.randint(0,numCols)
        x0 = builderRow*30
        y0 = builderCol*30
        x1 = builderRow*30 + 30
        y1 = builderCol*30 + 30
        return Builder(x0,y0,x1,y1)
        
    def isCollidingWithDot(self,other):
        if not isinstance(other,Dot):
            return False
        else:
            dist = ((other.cx - self.cx)**2 + (other.cy - self.cy)**2)**0.5
            return dist < self.r + other.r
                

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.board = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0
, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1
, 1, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0
, 0, 1], [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0,
 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1,
 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 
1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0
, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1,
 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 
1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    data.numRows = data.height//30
    data.numCols = data.width//30
    data.pacman = Pacman(210,210)
    data.score = 0
    data.builders = []
    data.mode = "start"
    data.timerCalls = 0
    data.minDist = 8
    data.maxDist = 12
    data.numBuilders = 4
    data.dots = []
    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            if data.board[row][col] == 1:
                data.dots.append(Dot(row*30+15,col*30+15))
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if data.mode == "start":
        startScreenKeyPressed(event,data)
    elif data.mode == "play":
        playKeyPressed(event,data)
    # use event.char and event.keysym
    

def timerFired(data):
    data.pacman.move()
    data.timerCalls += 1
    if data.mode == "play":
        pacCol = int(data.pacman.row)
        pacRow = int(data.pacman.col)
        if data.board[pacRow][pacCol] == 1:
            data.board[pacRow][pacCol] = 2
            data.score += 1
            
    
def redrawAll(canvas, data):
    # draw in canvas
    if data.mode == "start":
        startScreenRedrawAll(canvas,data)
    elif data.mode == "play":
        playRedrawAll(canvas,data)
    
    
### start screen ###

def startScreenKeyPressed(event,data):
    data.mode = "play"
    
def startScreenRedrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="black")
    canvas.create_text(data.width//2,data.height//2-30,text="Building instructions: Press space to add another builder, maximum is 5",fill="white")
    canvas.create_text(data.width//2,data.height//2,text="Press any key to play",fill="white")
    
def startScreenTimerFired(data):
    pass
    
### play screen ###

def playKeyPressed(event,data):
    if event.keysym == "Right":
        data.pacman.direction = "Right"
    elif event.keysym == "Left":
        data.pacman.direction = "Left"
    elif event.keysym == "Up":
        data.pacman.direction = "Up"
    elif event.keysym == "Down":
        data.pacman.direction = "Down"
        
def playRedrawAll(canvas,data):
    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            if data.board[row][col] == 0:
                color = "black"
                canvas.create_rectangle(row*30,col*30,row*30+30,col*30+30,fill=color,outline=color)
            elif data.board[row][col] == 1:
                #print(row,col)
                color = "white"
                canvas.create_rectangle(row*30,col*30,row*30+30,col*30+30,fill=color,outline=color)
                canvas.create_oval(row*30+13,col*30+13,row*30+17,col*30+17,fill="green")
            elif data.board[row][col] == 2:
                color = "white"
                canvas.create_rectangle(row*30,col*30,row*30+30,col*30+30,fill=color,outline=color)
    data.pacman.draw(canvas)
    canvas.create_text(0,0,text="Score: " + str(data.score),anchor=NW,fill="blue")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
    
run(750, 600)