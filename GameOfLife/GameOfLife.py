# Game Of Life

'''Imports'''

# For random distribution of cells
from random import choice
from Tkinter import *

''''TKinter'''

class GameWindow(Frame):
  
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
        gridWidthScale = Scale(self, label="Grid width", orient="horizontal", from_=5, to=40, command=self.setGridWidth)
        gridWidthScale.grid(row=0)
        gridLengthScale = Scale(self, label="Grid length", orient="horizontal", from_=5, to=40, command=self.setGridLength)
        gridLengthScale.grid(row=1)
        numOfCellsScale = Scale(self, label="Starting cells", orient="horizontal", from_=10, to=200, command=self.setNumOfCells)
        numOfCellsScale.grid(row=2)
        
        #Game buttons
        placeCellsButton = Button(self, text = "New Grid", command = self.randomlyPlaceCells)
        placeCellsButton.grid(row=3)
        nextStepButton = Button(self, text = "Next Step", command = self.nextStep)
        nextStepButton.grid(row=3, column=1)
        stillLifeButton = Button(self, text = "Still Life", command = self.stillLife)
        stillLifeButton.grid(row=3, column=2)

        
        # Game grid
        self.gameCanvas = Canvas(self)
        self.gameCanvas.grid(row=0, column=1, rowspan=3, columnspan=2)

    def setGridWidth(self, val):
        self.gridWidth = int(float(val))

    def setGridLength(self, val):
        self.gridLength = int(float(val))
        
    def setNumOfCells(self, val):
        self.numOfCells = int(float(val))
    
    # Sets up grid and randomly places a given number of cells.
    
    def randomlyPlaceCells(self):
        # Check to see if too many cells are selected
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
            j = 0
            i += 1
        
        # Flip the given number of dead cells to life
        # Random cells are picked using the choice function
        n = 0
        while n < self.numOfCells:
            x = choice(self.grid)
            y = choice(x)
            if y.isAliveBool == False:
                y.isAliveBool = True
                y.willLoveBool = True
                n += 1
                
        # Change canvas size to fit grid and draw cells.
        self.gameCanvas.config(width = (5 * self.gridWidth ), height = (5 * self.gridLength))
        
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
                    self.gameCanvas.create_oval((5 * cell.xPosInt), (5 * cell.yPosInt), ((5 * cell.xPosInt) + 5), ((5 * cell.yPosInt) + 5), fill="red")
    
    # Advances grid by one step
    def nextStep(self):
        print "Next"
        # First, each cell checks its next step
        breakBool = False
        while breakBool == False:
            for column in self.grid:
                for cell in column:
                    cell.checkNextStep(self.grid)
                    print "Check",cell.xPosInt,cell.yPosInt,self.gridWidth,self.gridLength,breakBool
                    if (cell.xPosInt == (self.gridWidth -1)) and (cell.yPosInt == (self.gridLength -1)):
                        breakBool = True
        # Then each cell changes its state accordingly
        breakBool = False
        while breakBool == False:
            for column in self.grid:
                for cell in column:
                    cell.doNextStep()
                    print "Do"
                    if cell.xPosInt == (self.gridWidth -1) and cell.yPosInt == (self.gridLength -1):
                        breakBool = True
        # Finally the new canvas is drawn
        self.printGrid()
    
    def stillLife(self):
        pass

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

    def getAdjacentCells(self, grid):
        i = 0
        for column in grid:
            for otherCells in column:
                if ((otherCells.xPosInt == self.xPosInt) or (otherCells.xPosInt == self.xPosInt + 1) or (otherCells.xPosInt == self.xPosInt -1)) and ((otherCells.yPosInt == self.yPosInt) or (otherCells.yPosInt == self.yPosInt + 1) or (otherCells.yPosInt == self.yPosInt -1)) and (otherCells.isAliveBool == True):
                    i += 1
            if self.isAliveBool == True:
                return (i-1)
            else:
                return i
    # Changes the cell state
    def doNextStep(self):
        self.isAliveBool = self.willLiveBool

'''Functions'''
'''
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
            x.willLoveBool = True
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
'''
'''Main Program'''
#numOfCells=100, gridLength=20, gridWidth=20
def main():
    root = Tk()
    root.geometry("800x600+300+300")
    app = GameWindow(root)
    root.mainloop()
    '''  
    myGrid = []
    setUpGrid(gridLength, gridWidth, myGrid)
    randomlyPlaceLivingCells(numOfCells, myGrid)
    printTheGrid(myGrid)
    print "\n"
    nextStep(myGrid)'''
    
if __name__ == "__main__":
    main()
