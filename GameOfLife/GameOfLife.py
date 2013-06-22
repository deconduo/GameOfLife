# Game Of Life

'''Imports'''

# For random distribution of cells
from random import choice
from Tkinter import *

''''TKinter'''

class gameWindow(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Conway's Game Of Life")
        
        self.pack(fill=BOTH, expand=1)

        
        # Menu
        gameMenu = Menu(self.parent)
        self.parent.config(menu=gameMenu)        
        fileMenu = Menu(gameMenu)
        fileMenu.add_command(label="Save State", command=self.onExit)
        fileMenu.add_command(label="Load State", command=self.onExit)
        fileMenu.add_command(label="Exit", command=self.onExit)
        gameMenu.add_cascade(label="File", menu=fileMenu)
        
        # Game sliders
        gridWidth = Scale(self, label="Set grid width", orient="horizontal", from_=0, to=100, command=self.setGridWidth)
        gridWidth.grid(row=1)
        gridLength = Scale(self, label="Set grid length", orient="horizontal", from_=0, to=100, command=self.setGridLength)
        gridLength.grid(row=2)
        numOfCells = Scale(self, label="Set number of starting cells", orient="horizontal", from_=0, to=100, command=self.setNumOfCells)
        numOfCells.grid(row=3)
        
        # Game grid
        gameCanvas = Canvas(self)
        gameCanvas.grid(row=1, column=2, rowspan=3, columnspan=10)


    def setGridWidth(self, val):
        v = int(float(val))
        
    def setGridLength(self, val):
        v = int(float(val))
        
    def setNumOfCells(self, val):
        v = int(float(val))


    def onExit(self):
        self.quit()

'''Classes'''

# Defines the cell class
class cell(object):
    # Initialization function
    def __init__(self, xPos, yPos, isAlive=False, willLive=False):
        self.xPosInt = xPos
        self.yPosInt = yPos
        self.isAliveBool = isAlive
        self.willLiveBool = willLive
    
    # Checks if cell state will change with next step    
    def checkNextStep(self, grid):
        i = getAdjacentCells(self, grid)
        if self.isAliveBool == True:
            if (i < 2) or (i > 3):
                self.willLiveBool = False
        if self.isAliveBool == False:
            if i == 3:
                self.willLiveBool = True

    # Changes the cell state
    def doNextStep(self):
        self.isAliveBool = self.willLiveBool
        self.willLiveBool = False


'''Functions'''

# Sets up a blank grid
def setUpGrid(n, m, grid):
    i = 0
    j = 0
    while j < m :
        while i < n:
            grid.append(cell(i, j, False))
            i += 1
        i = 0
        j += 1    

# Places the given number of cells randomly on the board
def randomlyPlaceLivingCells(n, grid):
    i = 0
    while i < n:
        x = choice(grid)
        if x.isAliveBool == False:
            x.isAliveBool = True
            i += 1

# Prints the grid to the screen
def printTheGrid(grid):
    gridString = ""
    currentRow = 0
    for cell in grid:
        if cell.yPosInt != currentRow:
            gridString += "\n"
            currentRow += 1
        if cell.isAliveBool == True:
            gridString += "*"
        else:
            gridString += "-"
    print gridString

# Calculates the number of adjacent living cells for a given cell
def getAdjacentCells(cell, grid):
    i = 0
    for otherCells in grid:
        if ((otherCells.xPosInt == cell.xPosInt) or (otherCells.xPosInt == cell.xPosInt + 1) or (otherCells.xPosInt == cell.xPosInt -1)) and ((otherCells.yPosInt == cell.yPosInt) or (otherCells.yPosInt == cell.yPosInt + 1) or (otherCells.yPosInt == cell.yPosInt -1)) and (otherCells.isAliveBool == True):
            i += 1
    if cell.isAliveBool == True:
        return (i-1)
    else:
        return i
        
# Advances the board by one step
def nextStep(grid):
    for cell in grid:
        cell.checkNextStep(grid)
    for cell in grid:
        cell.doNextStep()
    printTheGrid(grid)

# Checks if the grid is empty
def isEmptyGrid(grid):
    isEmpty = True
    for cell in grid:
        if cell.isAliveBool == True:
            isEmpty = False
    return isEmpty

'''Main Program'''

def main(numOfCells=100, gridLength=20, gridWidth=20):
    root = Tk()
    root.geometry("250x150+300+300")
    app = gameWindow(root)
    root.mainloop()

    
    myGrid = []
    setUpGrid(gridLength, gridWidth, myGrid)
    randomlyPlaceLivingCells(numOfCells, myGrid)
    printTheGrid(myGrid)
    print "\n"
    nextStep(myGrid)
    
if __name__ == "__main__":
    main()
