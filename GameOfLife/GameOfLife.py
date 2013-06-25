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
        gridWidth.grid(row=1, column=1, columnspan=2)
        gridLength = Scale(self, label="Set grid length", orient="horizontal", from_=0, to=100, command=self.setGridLength)
        gridLength.grid(row=2, column=1, columnspan=2)
        numOfCells = Scale(self, label="Set number of starting cells", orient="horizontal", from_=0, to=100, command=self.setNumOfCells)
        numOfCells.grid(row=3, column=1, columnspan=2)
        
        # Game buttons
        
        myGrid = []
        gridWidth = 0
        gridLength = 0
        numOfCells = 0
        
        nextStepButton = Button(self, text="Next Step", command=self.nextStep(myGrid))
        nextStepButton.grid(row=4, column=3)
        
        setupButton = Button(self, text="Set Up Grid", command=self.setUpGrid(gridWidth, gridLength, numOfCells, myGrid))
        setupButton.grid(row=4, column=4)
        
        # Game grid
        gameCanvas = Canvas(self)
        gameCanvas.grid(row=1, column=3, rowspan=3, columnspan=10)

    def setGridWidth(self, val):
        gridWidth = int(float(val))
        
    def setGridLength(self, val):
        gridLength = int(float(val))
        
    def setNumOfCells(self, val):
        numOfCells = int(float(val))

        # Sets up a blank grid
    def setUpGrid(self, n, m, numCell, grid):
        i = 0
        j = 0
        while j < m :
            while i < n:
                grid.append(cell(i, j, False))
                i += 1
                i = 0
                j += 1
                self.randomlyPlaceLivingCells(numCell, grid)
                self.printTheGrid(grid)

    # Places the given number of cells randomly on the board
    def randomlyPlaceLivingCells(self, n, grid):
        i = 0
        while i < n:
            x = choice(grid)
            if x.isAliveBool == False:
                x.isAliveBool = True
                i += 1
    
    # Prints the grid to the screen
    def printTheGrid(self, grid):
        currentRow = 0
        for cell in grid:
            if cell.isAliveBool == True:
                gameCanvas.create_polygon((5*cell.xPosInt), (5*cell.yPosInt), (5*cell.xPosInt), (5*cell.yPosInt +5) ,(5*cell.xPosInt +5), (5*cell.yPosInt), (5*cell.xPosInt +5), (5*cell.yPosInt +5), fill="white")
            else:
                gameCanvas.create_polygon((5*cell.xPosInt), (5*cell.yPosInt), (5*cell.xPosInt), (5*cell.yPosInt +5) ,(5*cell.xPosInt +5), (5*cell.yPosInt), (5*cell.xPosInt +5), (5*cell.yPosInt +5), fill="red")
    
    # Calculates the number of adjacent living cells for a given cell
    def getAdjacentCells(self, cell, grid):
        i = 0
        for otherCells in grid:
            if ((otherCells.xPosInt == cell.xPosInt) or (otherCells.xPosInt == cell.xPosInt + 1) or (otherCells.xPosInt == cell.xPosInt -1)) and ((otherCells.yPosInt == cell.yPosInt) or (otherCells.yPosInt == cell.yPosInt + 1) or (otherCells.yPosInt == cell.yPosInt -1)) and (otherCells.isAliveBool == True):
                i += 1
        if cell.isAliveBool == True:
            return (i-1)
        else:
            return i
            
    # Advances the board by one step
    def nextStep(self, grid):
        for cell in grid:
            cell.checkNextStep(grid)
        for cell in grid:
            cell.doNextStep()
        self.printTheGrid(grid)
    
    # Checks if the grid is empty
    def isEmptyGrid(self, grid):
        isEmpty = True
        for cell in grid:
            if cell.isAliveBool == True:
                isEmpty = False
        return isEmpty
    
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



'''Main Program'''

def main():
    root = Tk()
    root.geometry("600x400+300+300")
    app = gameWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
