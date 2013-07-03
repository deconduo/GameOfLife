# Game Of Life

'''Imports'''

# For random distribution of cells
from random import choice
# For interface
from Tkinter import *

''''TKinter'''

# TKinter window class
class GameWindow(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        # Start UI, add window Title
        self.parent.title("Conway's Game Of Life")
        self.pack(fill=BOTH, expand=1)

        # Menu
        gameMenu = Menu(self.parent)
        self.parent.config(menu=gameMenu)        
        fileMenu = Menu(gameMenu)
        fileMenu.add_command(label="Exit", command=self.onExit)
        gameMenu.add_cascade(label="File", menu=fileMenu)
        
        # Game sliders
        gridWidthScale = Scale(self, label="Grid width", orient="horizontal", from_=1, to=40, command=self.setGridWidth)
        gridWidthScale.grid(row=0)
        gridLengthScale = Scale(self, label="Grid length", orient="horizontal", from_=1, to=40, command=self.setGridLength)
        gridLengthScale.grid(row=1)
        numOfCellsScale = Scale(self, label="Starting cells", orient="horizontal", from_=1, to=400, command=self.setNumOfCells)
        numOfCellsScale.grid(row=2)
        
        # Game buttons
        placeCellsButton = Button(self, text = "New Grid", command = self.randomlyPlaceCells)
        placeCellsButton.grid(row=3)
        nextStepButton = Button(self, text = "Next Step", command = self.nextStep)
        nextStepButton.grid(row=3, column=1)
        stillLifeButton = Button(self, text = "Still Life", command = self.stillLife)
        stillLifeButton.grid(row=3, column=2)

        # Game grid
        self.gameCanvas = Canvas(self)
        self.gameCanvas.grid(row=0, column=1, rowspan=3, columnspan=2)

    # Set values from sliders
    def setGridWidth(self, val):
        self.gridWidth = int(float(val))

    def setGridLength(self, val):
        self.gridLength = int(float(val))
        
    def setNumOfCells(self, val):
        self.numOfCells = int(float(val))
    
    # Sets up a blank grid
    def setUpGrid(self):
    # Check to see if too many cells are selected on the slider
        if self.numOfCells > (self.gridWidth * self.gridLength):
            self.numOfCells = (self.gridWidth * self.gridLength)
        # Set up empty grid
        self.grid = []
        # Set blank variables
        column = []
        i = 0
        j = 0
        # Fill grid with appropriate number of (dead) cells
        while i < self.gridWidth:
            while j < self.gridLength:
                cell = Cell(i, j)
                column.append(cell)
                j += 1
            self.grid.append(column)
            column = []
            j = 0
            i += 1
            
    # Sets up a grid and randomly places a given number of cells.
    def randomlyPlaceCells(self):
        # First set up a blank grid
        self.setUpGrid()        
        # Flip the given number of dead cells to life
        # Random cells are picked using the choice function
        n = 0
        while n < self.numOfCells:
            x = choice(self.grid)
            y = choice(x)
            if y.isAliveBool == False:
                y.isAliveBool = True
                y.willLiveBool = True
                n += 1
                
        # Change canvas size to fit grid and draw cells.
        self.gameCanvas.config(width = ((10 * self.gridWidth)+5 ), height = ((10 * self.gridLength))+5)
        
        # Print the grid to the canvs
        self.printGrid()
    
    # Prints the grid to the canvas
    def printGrid(self):
        # Clear the canvas first
        self.gameCanvas.delete(ALL)
        # Draw a circle for each living cell
        for column in self.grid:
            for cell in column:
                if cell.isAliveBool == True:
                    self.gameCanvas.create_oval(((10 * cell.xPosInt)+5), ((10 * cell.yPosInt)+5), ((10 * cell.xPosInt) + 15), ((10 * cell.yPosInt) + 15), fill="red")
    
    # Advances grid by one step
    def nextStep(self):
        # First, each cell checks its next step
        for column in self.grid:
            for cell in column:
                cell.checkNextStep(self.grid)
        # Then each cell changes its state accordingly
        for column in self.grid:
            for cell in column:
                cell.doNextStep()
        # Finally the new canvas is drawn
        self.printGrid()
    
    # Should only be done with small grid size!
    def stillLife(self):
        # First set up a blank grid
        self.setUpGrid()
        for x in combinations(self.grid, self.numOfCells):
            print x

    # Exit command
    def onExit(self):
        self.quit()

'''Classes'''
# Defines the cell class
class Cell(object):
    # Initialization function
    def __init__(self, xPos, yPos, isAlive=False, willLive=False):
        self.xPosInt = xPos
        self.yPosInt = yPos
        self.isAliveBool = isAlive
        self.willLiveBool = willLive
    
    def __str__(self):
        if self.isAliveBool == True:
            return "*"
        else:
            return "-"
    
    # Checks if cell state will change with next step    
    def checkNextStep(self, grid):
        # First it checks for the number of adjacent living cells
        nearbyCells = self.getAdjacentCells(grid)
        # If cell is alive, check if it dies
        if self.isAliveBool == True:
            if (nearbyCells < 2) or (nearbyCells > 3):
                self.willLiveBool = False
        # If cell is dead, check if it lives
        if self.isAliveBool == False:
            if nearbyCells == 3:
                self.willLiveBool = True
                
    # Method to check for adjacent cells
    def getAdjacentCells(self, grid):
        i = 0
        # Gets the number of living cells in a 3x3 grid around the selected cell
        for column in grid:
            for otherCells in column:
                if ((otherCells.xPosInt == self.xPosInt) or (otherCells.xPosInt == self.xPosInt + 1) or (otherCells.xPosInt == self.xPosInt -1)) and ((otherCells.yPosInt == self.yPosInt) or (otherCells.yPosInt == self.yPosInt + 1) or (otherCells.yPosInt == self.yPosInt -1)) and (otherCells.isAliveBool == True):
                    i += 1
        # If the selected cell is alive, return the count -1, as current cell is included in the count.
        if self.isAliveBool == True:
            return (i-1)
        # Otherwise simply return the count
        else:
            return i

    # Method to change the cell state for the next step.
    def doNextStep(self):
        self.isAliveBool = self.willLiveBool

'''Functions'''

# from python.org, http://docs.python.org/library/itertools.html
# the equivalent for itertools.combinations in a version of Python
# less than 2.6
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
            else:
                return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
'''Main Program'''

def main():
    # Sets up the TKinter window
    root = Tk()
    root.geometry("600x500+300+300")
    app = GameWindow(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
