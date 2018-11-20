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
            elif self.direction == "Left":
                self.cx -= self.speed
            elif self.direction == "Up":
                self.cy -= self.speed
            elif self.direction == "Down":
                self.cy += self.speed
    
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
    data.board = []
    data.numRows = data.width//30
    data.numCols = data.height//30
    for row in range(data.numRows): data.board += [[0]*data.numCols]
    data.pacman = Pacman(data.width//2,data.height//2)
    data.score = 0
    data.builders = []
    data.spawners = []
    data.mode = "start"
    data.timerCalls = 0
    data.minDist = 8
    data.maxDist = 12
    data.numBuilders = 8
    for i in range(data.numBuilders):
        data.builders.append(data.pacman.addBuilder())
    for builder in data.builders:
        builder.addSpawners()
    data.selected = []
    data.dots = []
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if data.mode == "start":
        startScreenKeyPressed(event,data)
    elif data.mode == "build":
        buildKeyPressed(event,data)
    elif data.mode == "play":
        playKeyPressed(event,data)
    # use event.char and event.keysym
    

def timerFired(data):
    data.timerCalls += 1
    if data.timerCalls > 50:
        data.mode = "play"
    x0 = data.pacman.cx - data.pacman.r
    y0 = data.pacman.cy - data.pacman.r
    x1 = data.pacman.cx + data.pacman.r
    y1 = data.pacman.cy + data.pacman.r
    data.pacman.move()
    if data.mode == "build": 
        for builder in data.builders:
            for spawner in builder.spawners:
                if ((spawner.x0//30+1,spawner.y0//30+1) not in data.selected or (spawner.x0//30-1,spawner.y0//30-1) not in data.selected) and spawner.x0//30>=0 and data.timerCalls <= 30:
                    spawner.moveSpawner()
                    if (spawner.x0//30,spawner.y0//30) not in data.selected and (0<=spawner.x0//30 <= data.numRows-1) and (0<=spawner.y0//30 <= 19):
                        data.selected.append((spawner.x0//30,spawner.y0//30))
                        spawner.distTraveled += 1
                        if (spawner.distTraveled == spawner.distance):
                            spawner.turnSpawner()
                            spawner.distTraveled = 0
                        if (spawner.x0//30 >= data.numRows or spawner.x0//30 <= 0) and (spawner.direction == "Right" or spawner.direction == "Left"):
                            spawner.direction = random.choice(["Up","Down"])
                        if (spawner.y0//30 >= data.numCols or spawner.y0//30 <= 0) and (spawner.direction == "Up" or spawner.direction == "Down"):
                            spawner.direction = random.choice(["Right","Left"])
    if data.mode == "play":
        for row in range(len(data.board)):
            for col in range(len(data.board[row])):
                if data.board[row][col] == 1:
                    data.dots.append(Dot(row*30+15,col*30+15))
        for dot in data.dots:
            if data.pacman.isCollidingWithDot(dot):
                
                data.board[row][col] = 2
                data.dots.remove(dot)
                data.score += 1
                break
            
    
def redrawAll(canvas, data):
    # draw in canvas
    if data.mode == "start":
        startScreenRedrawAll(canvas,data)
    if data.mode == "build":
        buildRedrawAll(canvas,data)
    elif data.mode == "play":
        playRedrawAll(canvas,data)
    
    
### start screen ###

def startScreenKeyPressed(event,data):
    data.mode = "build"
    
def startScreenRedrawAll(canvas,data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="black")
    canvas.create_text(data.width//2,data.height//2-30,text="Building instructions: Press space to add another builder, maximum is 5",fill="white")
    canvas.create_text(data.width//2,data.height//2,text="Press any key to play",fill="white")
    
def startScreenTimerFired(data):
    pass
    
### build screen ###

def buildKeyPressed(event,data):
    pass
        
def buildRedrawAll(canvas,data):
    # for row in range(data.numRows):
    #     for col in range(data.numCols):
    #         if (row,col) in data.selected:
    #             color = "white"
    #         else:
    #             color = "black"
    #         canvas.create_rectangle(row*30,col*30,row*30+30,col*30+30,fill=color,outline=color)
    for builder in data.builders:
        #builder.drawBuilder(canvas)
        if (builder.x0//30,builder.y0//30) not in data.selected and (0<=builder.x0//30 <= data.numRows-1) and (0<=builder.y0//30 <= 19):
            data.selected.append((builder.x0//30,builder.y0//30))
        for spawner in builder.spawners:
            spawner.drawSpawner(canvas)
            if (spawner.x0//30,spawner.y0//30) not in data.selected and (0<=spawner.x0//30 <= data.numRows-1) and (0<=spawner.y0//30 <= 19):
                data.selected.append((spawner.x0//30,spawner.y0//30))
    canvas.create_text(0,0,text="Building map...",fill="black",anchor=NW)
    for coord in set(data.selected):
        data.board[coord[0]][coord[1]] = 1
        
        
    
    
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
            else:
                color = "white"
            canvas.create_rectangle(row*30,col*30,row*30+30,col*30+30,fill=color,outline=color)
    for dot in data.dots:
        dot.drawDot(canvas)
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